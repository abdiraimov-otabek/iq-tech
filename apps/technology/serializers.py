from rest_framework import serializers

from apps.technology.models import Technology


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = [
            'id',
            'name_uz',
            'name_ru',
            'name_en',
            'icon'
        ]