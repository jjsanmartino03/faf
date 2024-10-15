from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response



# Create your views here.
class GetAuthenticatedUser(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        user = request.user

        data = {
            'username': user.username,
            'is_staff': user.is_staff,
            'team_id': user.team_id,
        }
        return Response(data)
