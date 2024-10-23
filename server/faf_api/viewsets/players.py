import os.path

                       
from django.core.files.base import ContentFile
from django.http.multipartparser import MultiPartParser
from rest_framework import serializers, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action

from faf_api.models import Players, PlayerImages
from rest_framework.response import Response

from faf_api.services.vision import VisionService


class PlayersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Players
        fields = '__all__'


class PlayersViewSet(viewsets.ModelViewSet):

    authentication_classes = [TokenAuthentication]
    permission_classes = []

    queryset = Players.objects.all()
    serializer_class = PlayersSerializer

    def get_queryset(self):
        queryset = Players.objects.all().order_by('name')
        if self.action == 'list':
            team_category_id = self.request.query_params.get('team_category_id', None)
            if team_category_id is not None:
                queryset = queryset.filter(team_category_id=team_category_id)
            else:
                raise Exception('team_category_id is required')
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        result = []
        for player in serializer.data:
            images = PlayerImages.objects.filter(player_id=player['id'])
            player['image'] = images[0].image if images else None
            result.append(player)
        return Response(result)

    def retrieve(self, request, *args, **kwargs):
        player = self.get_object()

        images = PlayerImages.objects.filter(player_id=player.id)
        image_ids = [{
            'id': image.id,
            'image': image.image
        } for image in images]

        return Response({'id': player.id, 'name': player.name, 'status': player.status, 'images': image_ids})

    def update(self, request, *args, **kwargs):
        data = request.data
        player_id = kwargs.get('pk')
        player = Players.objects.get(id=player_id)

        if data.get('name'):
            player.name = data['name']
        if data.get('status') is not None:
            user = request.user
            player.status = data.get('status')
            if not user.is_staff:
                return Response({'error': 'Only staff can change status'}, status=403)
        player.save()

        return Response({'id': player.id, 'name': player.name})

    @action(detail=True, methods=['post'], url_path='image')
    def upload_image(self, request, pk=None):
        player = self.get_object()
        image = request.data.get('image')

        if not image:
            return Response({'error': 'No image provided'}, status=400)

        # is png or jpg?
        if image.content_type not in ['image/jpeg', 'image/png']:
            return Response({'error': 'Invalid image format'}, status=400)

        imageEntity = PlayerImages.objects.create(player=player)
        imageEntity.save()

        if image.content_type == 'image/jpeg':
            imageEntity.image = f'{imageEntity.id}.jpg'
        else:
            imageEntity.image = f'{imageEntity.id}.png'

        # save in folder /images/players/{image.id}.{jpg/png}

        # Save the image using default_storage
        relative_path = default_storage.save(f'players/{player.id}/{imageEntity.image}', ContentFile(image.read()))
        imageEntity.save()

        real_image_path = os.path.join(
            default_storage.location,
            relative_path
        )

        vision_service = VisionService()
        vision_service.train_new_player_image(real_image_path, player.id)

        return Response({'status': 'image uploaded', 'path': relative_path}, status=200)
