from django.shortcuts import render
from rest_framework import viewsets

from apps.technology.models import Technology
from apps.technology.serializers import TechnologySerializer


class TechnologyViewSet(viewsets.ModelViewSet):
    queryset = Technology
    serializer_class = TechnologySerializer
