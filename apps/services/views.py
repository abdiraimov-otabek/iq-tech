from rest_framework import viewsets

from apps.services.models import Service
from apps.services.serializers import ServiceSerializer


class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
