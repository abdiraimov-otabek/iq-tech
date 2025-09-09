from django.urls import path

from apps.blog.views import BlogPostViewList

urlpatterns = [
    path("", BlogPostViewList.as_view(), name="blog_posts")
]