from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TeamMembersViewSet

router = DefaultRouter()
router.register(r"team_members", TeamMembersViewSet, basename="team_member")

urlpatterns = [
    path("", include(router.urls))
]