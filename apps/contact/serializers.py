from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            "id",
            "name",
            "phone_number",
            "request",
        ]

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError(_("Title bo‘sh bo‘lishi mumkin emas"))
        return value