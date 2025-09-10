from django.urls import path

from apps.blog.views import BlogPostViewList, BlogPostSlugView

urlpatterns = [
    path("", BlogPostViewList.as_view(), name="blog_posts"),
    path("<slug:slug>/", BlogPostSlugView.as_view(), name="blog_post_detail")
]