from django.urls import path

from .views import ServicesViewList, ServicesSlugView

urlpatterns = [
    path("", ServicesViewList.as_view(), name="services"),
    path("<slug:slug>/", ServicesSlugView.as_view(), name="services_detail")
]