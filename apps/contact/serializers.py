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

    def validate(self, attrs):
        if not attrs.get("name") and not attrs.get("phone_number"):
            raise serializers.ValidationError(_("Нужно заполнить хотя бы имя или телефон"))
        return attrs