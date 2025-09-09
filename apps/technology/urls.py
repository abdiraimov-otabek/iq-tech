from django.urls import path

from .views import TechnologyViewList


urlpatterns = [
    path("", TechnologyViewList.as_view(), name="technology")
]