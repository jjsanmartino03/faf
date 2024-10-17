from rest_framework import serializers, viewsets

from faf_api.models import Players
from rest_framework.response import Response


class PlayersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Players
        fields = '__all__'


class PlayersViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []

    queryset = Players.objects.all()
    serializer_class = PlayersSerializer

    def get_queryset(self):
        queryset = Players.objects.all()
        team_category_id = self.request.query_params.get('team_category_id', None)
        if team_category_id is not None:
            queryset = queryset.filter(team_category_id=team_category_id)
        else:
            raise Exception('team_category_id is required')
        return queryset

    def update(self, request, *args, **kwargs):
        data = request.data
        player_id = kwargs.get('pk')
        player = Players.objects.get(id=player_id)
        player.name = data['name']
        player.save()
        return Response({'id': player.id, 'name': player.name})
