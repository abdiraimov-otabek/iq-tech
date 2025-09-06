from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.blog.views import BlogPostViewSet

router = DefaultRouter()
router.register(r"blog_posts", BlogPostViewSet, basename="blog_post")

urlpatterns = [
    path("", include(router.urls))
]