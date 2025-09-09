from django.urls import path

from apps.projects.views import ProjectViewList

urlpatterns = [
    path("", ProjectViewList.as_view(), name ="projects")
]