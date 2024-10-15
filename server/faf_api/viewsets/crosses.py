from datetime import datetime
from pprint import pprint

from django.db.models import Q
from rest_framework.response import Response
from rest_framework import serializers, viewsets

from faf_api.models import Crosses, Categories, Matches, TeamCategories, Validation, Teams
from faf_api.utils.validation_status import ValidationStatus


class MatchesValidationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Validation
        fields = '__all__'


class CrossesTeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = '__all__'


class CrossesMatchesSerializer(serializers.ModelSerializer):
    local_validation = MatchesValidationsSerializer(read_only=True)
    visitor_validation = MatchesValidationsSerializer(read_only=True)

    class Meta:
        model = Matches
        fields = '__all__'


class CrossesSerializer(serializers.ModelSerializer):
    matches = CrossesMatchesSerializer(many=True, read_only=True, source='matches_set')
    local_team = CrossesTeamsSerializer(read_only=True)
    visitor_team = CrossesTeamsSerializer(read_only=True)

    class Meta:
        model = Crosses
        fields = '__all__'


class CrossesViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []

    queryset = Crosses.objects.all()
    serializer_class = CrossesSerializer

    def create(self, request, *args, **kwargs):
        data = request.data

        if not data.get('date') or not data.get('local_team_id') or not data.get('visitor_team_id'):
            return Response({'error': 'Missing data'}, status=400)

        # validate if date is parseable and is at least today
        date_string = data.get('date')
        try:
            parsed_date = datetime.strptime(date_string + ' 00:00:00', '%Y-%m-%d %H:%M:%S')

            print(parsed_date)
            print(datetime.now().replace(hour=0, minute=0, second=0, microsecond=0))
            if parsed_date < datetime.now().replace(hour=0, minute=0, second=0, microsecond=0):
                return Response({'error': 'Invalid date', 'date': parsed_date,}, status=400)
        except ValueError:
            return Response({'error': 'Invalid date format'}, status=400)

        # check if teams exist
        local_team = TeamCategories.objects.filter(team_id=data.get('local_team_id'))
        visitor_team = TeamCategories.objects.filter(team_id=data.get('visitor_team_id'))

        if not local_team or not visitor_team:
            return Response({'error': 'Teams not found'}, status=404)

        cross = Crosses.objects.create(
            date=parsed_date.date(),
            local_team_id=data.get('local_team_id'),
            visitor_team_id=data.get('visitor_team_id'),
        )

        cross.save()

        active_categories = Categories.objects.filter(active=True)
        for category in active_categories:
            local_team_category = TeamCategories.objects.get(team_id=cross.local_team_id, category_id=category.id)
            visitor_team_category = TeamCategories.objects.get(team_id=cross.visitor_team_id, category_id=category.id)

            local_validation = Validation.objects.create(status=ValidationStatus.PENDING.value, photo=None)
            visitor_validation = Validation.objects.create(status=ValidationStatus.PENDING.value, photo=None)

            match = Matches.objects.create(
                cross=cross,
                category=category.year,
                local_team_category=local_team_category,
                visitor_team_category=visitor_team_category,
                local_validation=local_validation,
                visitor_validation=visitor_validation,
            )

            match.save()

        return Response(CrossesSerializer(cross).data)

    def list(self, request, *args, **kwargs):
        query_params = request.query_params

        crosses = Crosses.objects.filter(date__gte=datetime.now()).order_by('date')

        team_id = query_params.get('team_id')
        if team_id:
            crosses = crosses.filter(
                Q(local_team_id=team_id) | Q(visitor_team_id=team_id))

        team_name = query_params.get('team_name')
        if team_name:
            crosses = crosses.filter(
                Q(local_team__name__icontains=team_name) | Q(visitor_team__name__icontains=team_name))

        date_to_string = query_params.get('date_to')
        if date_to_string:
            try:
                date_to = datetime.strptime(date_to_string, '%Y-%m-%d')
                crosses = crosses.filter(date__lte=date_to)
            except ValueError:
                return Response({'error': 'Invalid date format'}, status=400)

        # todo: Deberíamos devolver únicamente las validaciones de su propio equipo si se
        # trata de un delegado, y todas las validaciones si se trata de un administrador.
        # Por ahora lo dejamos así pero es una mejora a realizar.

        return Response(CrossesSerializer(crosses, many=True).data)
