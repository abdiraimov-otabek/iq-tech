from rest_framework import viewsets

from apps.blog.models import BlogPost
from apps.blog.serializers import BlogPostSerializer


class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
