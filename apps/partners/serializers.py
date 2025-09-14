from rest_framework import serializers
from .models import Partner

class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = [
            "id",
            "name_uz",
            "name_ru",
            "name_en",
            "logo",
            "url",
            "created_at",
            "updated_at",
        ]