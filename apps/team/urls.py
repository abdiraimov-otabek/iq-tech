from django.urls import path

from .views import TeamMembersViewList, TeamMembersSlugView

urlpatterns = [
    path("", TeamMembersViewList.as_view(), name="team_members"),
    path("<slug:slug>/", TeamMembersSlugView.as_view(), name="team_members_detail")
]