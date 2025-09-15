from rest_framework import generics

from apps.services.models import Service
from apps.services.serializers import ServiceSerializer


class ServicesViewList(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServicesSlugView(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
