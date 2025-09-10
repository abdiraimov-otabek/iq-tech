from rest_framework import serializers
from .models import Project
from django.contrib.auth import get_user_model

from ..technology.serializers import TechnologySerializer

User = get_user_model()



class ProjectSerializer(serializers.ModelSerializer):
    tech_stack = TechnologySerializer(many=True, read_only=True)
    team = serializers.StringRelatedField(many=True, read_only=True)
    status = serializers.CharField(source="get_status_display", read_only=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "slug",
            "description",
            "image",
            "demo_url",
            "tech_stack",
            "team",
            "status",
            "created_at",
            "updated_at",
        ]
