from rest_framework import serializers
from .models import Role, TeamMember


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = [
            "id",
            "name",
            "created_at",
            "updated_at",
        ]


class TeamMemberSerializer(serializers.ModelSerializer):
    role = RoleSerializer(read_only=True)
    role_id = serializers.PrimaryKeyRelatedField(
        queryset=Role.objects.all(), source="role", write_only=True, required=False
    )

    class Meta:
        model = TeamMember
        fields = [
            "id",
            "first_name",
            "last_name",
            "slug",
            "role",
            "role_id",
            "bio",
            "photo",
            "email",
            "linkedin_url",
            "github_url",
            "is_active",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["slug", "created_at", "updated_at"]
