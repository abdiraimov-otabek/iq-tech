from rest_framework import serializers
from .models import Project, ProjectCategory
from django.contrib.auth import get_user_model

from ..technology.serializers import TechnologySerializer

User = get_user_model()

class ProjectCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectCategory
        fields = [
            "id",
            "name_uz",
            "name_ru",
            "name_en"
        ]

class ProjectSerializer(serializers.ModelSerializer):
    category = ProjectCategorySerializer(read_only=True)
    tech_stack = TechnologySerializer(many=True, read_only=True)
    team = serializers.StringRelatedField(many=True, read_only=True)
    status = serializers.CharField(source="get_status_display", read_only=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "slug",
            "description_uz",
            "description_ru",
            "description_en",
            "category",
            "image",
            "demo_url",
            "tech_stack",
            "team",
            "status",
            "created_at",
            "updated_at",
        ]
