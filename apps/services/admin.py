from unfold.admin import ModelAdmin
from django.contrib import admin
from .models import Service


@admin.register(Service)
class ServiceAdmin(ModelAdmin):
    list_display = ("title_uz", "created_at", "updated_at")
    search_fields = ("title_uz", "description_uz")
    readonly_fields = ("created_at", "updated_at")
    ordering = ("-created_at",)
