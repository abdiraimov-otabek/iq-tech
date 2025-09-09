from django.urls import path

from .views import StatisticViewList

urlpatterns = [
    path("", StatisticViewList.as_view(), name="statistics")
]