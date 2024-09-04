from rest_framework import serializers, viewsets, routers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from faf_api.models import Teams
from faf_api.models import Players


# Create your views here.
class GetAuthenticatedUser(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        user = request.user
        data = {
            'username': user.username,
            'is_staff': user.is_staff,
        }
        return Response(data)


class TeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = '__all__'
        


class TeamsViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Teams.objects.all()
    serializer_class = TeamsSerializer

class PlayersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Players
        fields = '__all__'

class PlayersViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []

    queryset = Players.objects.all()
    serializer_class = PlayersSerializer




router = routers.DefaultRouter()
router.register(r'teams', TeamsViewSet)
router.register(r'players', PlayersViewSet)
router.register(r'user', GetAuthenticatedUser, basename='user')
