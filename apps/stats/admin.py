from unfold.admin import ModelAdmin
from django.contrib import admin
from .models import Statistics


@admin.register(Statistics)
class StatisticsAdmin(ModelAdmin):
    list_display = (
        "total_projects",
        "total_clients",
        "years_experience",
        "team_members",
        "happy_customers",
        "created_at",
        "updated_at",
    )
    search_fields = (
        "total_projects",
        "total_clients",
        "years_experience",
        "team_members",
        "happy_customers",
    )
    readonly_fields = ("created_at", "updated_at")
    ordering = ("-updated_at",)
