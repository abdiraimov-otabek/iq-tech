from django.urls import path

from apps.projects.views import ProjectViewList, ProjectSlugView

urlpatterns = [
    path("", ProjectViewList.as_view(), name="projects"),
    path("<slug:slug/", ProjectSlugView.as_view(), name="project_detail")
]