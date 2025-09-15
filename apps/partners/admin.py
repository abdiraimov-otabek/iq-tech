from . import translation

from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from unfold.admin import ModelAdmin

from apps.partners.models import Partner



@admin.register(Partner)
class PartnersAdmin(TranslationAdmin,ModelAdmin):
    list_display = ("name","url")
    search_fields = ("name","-created_at")
    ordering = ("name",)