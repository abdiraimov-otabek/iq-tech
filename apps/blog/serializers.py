from rest_framework import serializers
from .models import BlogCategory, BlogPost


class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = [
            "id",
            "name_uz",
            "name_ru",
            "name_en",
            "slug",
            "description_uz",
            "description_ru",
            "description_en",
            "created_at",
        ]


class BlogPostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    category = BlogCategorySerializer(read_only=True)

    class Meta:
        model = BlogPost
        fields = [
            "id",
            "title_uz",
            "title_ru",
            "title_en",
            "slug",
            "author",
            "category",
            "content_uz",
            "content_ru",
            "content_en",
            "cover_image",
            "status",
            "is_featured",
            "published_at",
            "created_at",
            "updated_at",
        ]
