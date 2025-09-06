from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import StatisticViewSet

router = DefaultRouter()
router.register(r"statistics", StatisticViewSet, basename="statistic")

urlpatterns = [
    path("", include(router.urls))
]