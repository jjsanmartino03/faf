from rest_framework import serializers, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from faf_api.models import Teams, Categories, TeamCategories
from faf_api.models import Validation
from faf_api.services.vision import VisionService
from rest_framework.decorators import action
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os.path


class TeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = '__all__'


class TeamsViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = TeamsSerializer
    queryset = Teams.objects.all().order_by('name')

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

    @action(detail=True, methods=['post'], url_path='upload_image')
    def upload_image(self, request, pk=None):
        # Validar que el id de la validación exista
        try:
            validation = Validation.objects.get(pk=pk)
        except Validation.DoesNotExist:
            return Response({'error': 'Validation ID not found'}, status=404)
        # Obtener la imagen del request
        image = request.data.get('image')
        if not image:
            return Response({'error': 'No image provided'}, status=400)
        # Validar el formato de la imagen
        if image.content_type not in ['image/jpeg', 'image/png']:
            return Response({'error': 'Invalid image format'}, status=400)
        # Guardar la imagen en la ruta especificada
        extension = image.content_type.split('/')[-1]  # jpg o png
        image_name = f'{pk}.{extension}'
        relative_path = default_storage.save(f'validations/{image_name}', ContentFile(image.read()))
        real_image_path = os.path.join(default_storage.location, relative_path)
        # Pasar la ruta de la imagen al VisionService para validar
        vision_service = VisionService()

        team_id = request.user.team_id

        is_valid = vision_service.recognize_players_in_image(str(real_image_path), team_id)
        # Actualizar el estado de la validación
        validation.status = 'passed' if is_valid else 'failed'
        validation.save()
        # Responder según lo que se necesite
        response_data = {
            'validation_id': validation.id,
            'status': validation.status,
            'image_path': relative_path
        }
        return Response(response_data, status=200)
