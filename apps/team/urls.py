from django.urls import path

from .views import TeamMembersViewList

urlpatterns = [
    path("", TeamMembersViewList.as_view(), name="team_members")
]