from rest_framework import serializers
from .models import Statistics


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
