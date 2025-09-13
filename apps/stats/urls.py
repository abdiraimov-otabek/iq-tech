from django.urls import path

from .views import StatisticViewList, ReviewViewList

urlpatterns = [
    path("", StatisticViewList.as_view(), name="statistics"),
    path("reviews/", ReviewViewList.as_view(), name="reviews"),
]