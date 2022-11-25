
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializers import UploadSerializer
from .utils.parsedFile import parseField

class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer

    def list(self, request):
        return Response("GET API")

    def create(self, request):
        file_uploaded = request.FILES.get('file_uploaded')
        content_type = file_uploaded.content_type
        file = parseField(file_uploaded)
        response = "POST API and you have uploaded a {} file".format(content_type)
        return Response(file)