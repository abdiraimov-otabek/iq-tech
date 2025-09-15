from . import translation

from django.db import models
from modeltranslation.admin import TranslationAdmin
from unfold.admin import ModelAdmin
from django.contrib import admin
from unfold.contrib.forms.widgets import WysiwygWidget

from .models import Project


@admin.register(Project)
class ProjectAdmin(TranslationAdmin, ModelAdmin):
    list_display = (
        "title",
        "status",
        "created_at",
        "updated_at",
    )
    list_filter = ("status", "created_at", "tech_stack")
    search_fields = ("title", "description", "demo_url")
    filter_horizontal = ("tech_stack", "team")
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("created_at", "updated_at")
    ordering = ("-created_at",)
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        }
    }





