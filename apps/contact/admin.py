from unfold.admin import ModelAdmin
from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(ModelAdmin):
    list_display = ("name", "phone_number", "request")
    search_fields = ("name", "phone_number", "request")
    ordering = ("-id",)
    readonly_fields = ()
