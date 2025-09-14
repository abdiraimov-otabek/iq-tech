from django.urls import path

from apps.partners.views import PartnerViewList

urlpatterns = [
    path("", PartnerViewList.as_view(), name="partners")
]