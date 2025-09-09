from rest_framework import generics

from apps.projects.models import Project
from apps.projects.serializers import ProjectSerializer


class ProjectViewList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
