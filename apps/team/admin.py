from . import translation

from django.db import models
from modeltranslation.admin import TranslationAdmin
from unfold.admin import ModelAdmin
from django.contrib import admin
from unfold.contrib.forms.widgets import WysiwygWidget

from .models import Role, TeamMember


@admin.register(Role)
class RoleAdmin(TranslationAdmin, ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    search_fields = ("name",)
    readonly_fields = ("created_at", "updated_at")
    ordering = ("name",)


@admin.register(TeamMember)
class TeamMemberAdmin(TranslationAdmin, ModelAdmin):
    list_display = (
        "full_name",
        "email",
        "is_active",
        "created_at",
        "updated_at",
    )
    list_filter = ("role", "is_active", "created_at")
    search_fields = (
        "full_name",
        "email",
        "role__name",
    )
    readonly_fields = ("created_at", "updated_at", "slug")
    ordering = ["-created_at"]
    prepopulated_fields = {"slug": ("title",)}
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        }
    }
