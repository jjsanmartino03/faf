from rest_framework import routers

from faf_api.viewsets.crosses import CrossesViewSet
from faf_api.viewsets.players import PlayersViewSet
from faf_api.viewsets.teams import TeamsViewSet
from faf_api.viewsets.users import GetAuthenticatedUser
from faf_api.viewsets.validations_tests import ValidationTests

router = routers.DefaultRouter()
router.register(r'teams', TeamsViewSet)
router.register(r'players', PlayersViewSet)
router.register(r'user', GetAuthenticatedUser, basename='user')
router.register(r'crosses', CrossesViewSet)
router.register(r'validation-test', ValidationTests, basename='validation-test')
