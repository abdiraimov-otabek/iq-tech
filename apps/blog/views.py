from rest_framework import generics

from apps.blog.models import BlogPost
from apps.blog.serializers import BlogPostSerializer


class BlogPostViewList(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class BlogPostSlugView(generics.RetrieveAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = "slug"