from unfold.admin import ModelAdmin
from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(ModelAdmin):
    list_display = (
        "title",
        "status",
        "created_at",
        "updated_at",
    )
    list_filter = ("status", "created_at", "tech_stack")
    search_fields = ("title", "description", "demo_url")
    filter_horizontal = ("tech_stack", "team")
    readonly_fields = ("created_at", "updated_at")
    ordering = ("-created_at",)



