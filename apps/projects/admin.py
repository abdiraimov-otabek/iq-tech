from django.db import models
from unfold.admin import ModelAdmin
from django.contrib import admin
from unfold.contrib.forms.widgets import WysiwygWidget

from .models import Project


@admin.register(Project)
class ProjectAdmin(ModelAdmin):
    list_display = (
        "title_uz",
        "status",
        "created_at",
        "updated_at",
    )
    list_filter = ("status", "created_at", "tech_stack")
    search_fields = ("title_uz", "description", "demo_url")
    filter_horizontal = ("tech_stack", "team")
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("created_at", "updated_at")
    ordering = ("-created_at",)
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        }
    }
    fields = [
        "id",
        "title_uz",
        "title_ru",
        "title_en",
        "slug",
        "description_uz",
        "description_ru",
        "description_en",
        "image",
        "demo_url",
        "tech_stack",
        "team",
        "status",
        "created_at",
        "updated_at",
    ]




