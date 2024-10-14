from rest_framework import serializers, viewsets

from faf_api.models import Crosses


class CrossesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crosses
        fields = '__all__'


class CrossesViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []

    queryset = Crosses.objects.all()
    serializer_class = CrossesSerializer
