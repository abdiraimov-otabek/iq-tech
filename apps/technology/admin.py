from django.contrib import admin
from unfold.admin import ModelAdmin
from apps.technology.models import Technology


@admin.register(Technology)
class TechnologyAdmin(ModelAdmin):
    list_display = ("name_uz",)
    search_fields = ("name_uz",)
    ordering = ("name_uz",)