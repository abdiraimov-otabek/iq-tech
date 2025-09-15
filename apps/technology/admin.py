from . import translation

from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from unfold.admin import ModelAdmin
from apps.technology.models import Technology


@admin.register(Technology)
class TechnologyAdmin(TranslationAdmin, ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)