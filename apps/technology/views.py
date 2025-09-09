from rest_framework import generics

from apps.technology.models import Technology
from apps.technology.serializers import TechnologySerializer


class TechnologyViewList(generics.ListAPIView):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
