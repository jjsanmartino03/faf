from rest_framework import serializers, viewsets
from rest_framework.response import Response

from faf_api.models import Teams, Categories, TeamCategories


class TeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = '__all__'


class TeamsViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []

    queryset = Teams.objects.all()
    serializer_class = TeamsSerializer

    # overwrite the team create endpoint

    def create(self, request, *args, **kwargs):
        data = request.data
        team = Teams.objects.create(name=data['name'], logo_url=data['logo_url'])
        team.save()

        categories = Categories.objects.filter(active=True)

        for category in categories:
            team_category = TeamCategories.objects.create(team=team, category=category)
            team_category.save()

        return Response({'id': team.id, 'name': team.name})

    def retrieve(self, request, *args, **kwargs):
        team: Teams = self.get_object()

        categories = TeamCategories.objects.filter(team=team)
        team_data = TeamsSerializer(team).data

        categories_data = []
        for category in categories:
            categories_data.append({
                'id': category.id,
                'category': category.category.year
            })

        team_data['categories'] = categories_data

        return Response(team_data)
