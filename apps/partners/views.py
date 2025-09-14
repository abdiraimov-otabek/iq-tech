from django.shortcuts import render
from rest_framework import generics

from apps.partners.models import Partner
from apps.partners.serializers import PartnerSerializer


class PartnerViewList(generics.ListAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
