from rest_framework import serializers
from .models import BlogCategory, BlogPost


class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = [
            "id",
            "name",
            "slug",
            "description",
            "created_at",
        ]


class BlogPostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    category = BlogCategorySerializer(read_only=True)

    class Meta:
        model = BlogPost
        fields = [
            "id",
            "title",
            "slug",
            "author",
            "category",
            "content",
            "cover_image",
            "status",
            "is_featured",
            "published_at",
            "created_at",
            "updated_at",
        ]
