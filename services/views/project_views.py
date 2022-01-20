from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from services.serializers.project_serializer import ProjectSerializer
from services.models.project import Project

class ProjectAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        project_set = Project.objects.all()
        content = ProjectSerializer(project_set, many=True).data
        return Response(content)