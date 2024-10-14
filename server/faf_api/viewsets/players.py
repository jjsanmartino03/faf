from rest_framework import serializers, viewsets

from faf_api.models import Players


class PlayersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Players
        fields = '__all__'


class PlayersViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []

    queryset = Players.objects.all()
    serializer_class = PlayersSerializer
