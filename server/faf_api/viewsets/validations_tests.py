from rest_framework.response import Response

from faf_api.services.vision import VisionService
from rest_framework import viewsets

class ValidationTests(viewsets.ViewSet):
    authentication_classes = []
    permission_classes = []

    def create(self, request):
        image_path = request.data.get('image')

        if not image_path:
            return Response({'error': 'Image is required'}, status=400)

        vision_service = VisionService()
        result = vision_service.recognize_players_in_image(image_path)

        return Response({
            'status': result,
        })
