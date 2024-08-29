from django.shortcuts import render
from rest_framework import serializers, viewsets,routers

from faf_api.models import Teams


# Create your views here.
class TeamsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teams
        fields = '__all__'


class TeamsViewSet(viewsets.ModelViewSet):
    queryset = Teams.objects.all()
    serializer_class = TeamsSerializer


router = routers.DefaultRouter()
router.register(r'teams', TeamsViewSet)
