from django.urls import path

from .views import ServicesViewList


urlpatterns = [
    path("", ServicesViewList.as_view(), name="services")
]