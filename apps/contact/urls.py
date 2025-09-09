from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.contact.views import ContactCreateView

urlpatterns = [
    path("", ContactCreateView.as_view(), name="contacts")
]