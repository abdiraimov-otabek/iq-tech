from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TechnologyViewSet

router = DefaultRouter()
router.register(r"technologies", TechnologyViewSet, basename="technology")

urlpatterns = [
    path("", include(router.urls))
]