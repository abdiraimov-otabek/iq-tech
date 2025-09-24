from rest_framework import serializers
from .models import Statistics, Reviews


class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = [
            "id",
            "total_projects",
            "total_clients",
            "years_experience",
            "team_members",
            "happy_customers",
            "created_at",
            "updated_at",
        ]

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = [
            "id",
            "name_uz",
            "name_ru",
            "name_en",
            "image",
            "content_uz",
            "content_ru",
            "content_en",
            "created_at",
            "updated_at",
        ]