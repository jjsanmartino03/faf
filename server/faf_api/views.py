from rest_framework import serializers, viewsets, routers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from faf_api.models import Teams, Players, Categories, TeamCategories


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


class TeamCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamCategories
        # returnn category.year too
        fields = ['id', 'category']


class TeamsViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

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
