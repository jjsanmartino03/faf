from rest_framework import routers
from faf_api.viewsets.players import PlayersViewSet
from faf_api.viewsets.teams import TeamsViewSet
from faf_api.viewsets.users import GetAuthenticatedUser

router = routers.DefaultRouter()
router.register(r'teams', TeamsViewSet)
router.register(r'players', PlayersViewSet)
router.register(r'user', GetAuthenticatedUser, basename='user')
