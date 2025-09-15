from . import translation  # this is important so modeltranslation picks up

from django.db import models
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group

from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import WysiwygWidget

from modeltranslation.admin import TranslationAdmin

from .models import BlogCategory, BlogPost


# --- Unregister default User & Group ---
admin.site.unregister(User)
admin.site.unregister(Group)


# --- User & Group with unfold forms ---
@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass


# --- BlogCategory Admin with translations ---
@admin.register(BlogCategory)
class BlogCategoryAdmin(TranslationAdmin, ModelAdmin):
    list_display = ("name", "slug", "created_at")
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("name",)


# --- BlogPost Admin with translations ---
@admin.register(BlogPost)
class BlogPostAdmin(TranslationAdmin, ModelAdmin):
    list_display = (
        "title",
        "author",
        "category",
        "status",
        "is_featured",
        "published_at",
        "created_at",
    )
    list_filter = ("status", "is_featured", "category", "author")
    search_fields = ("title", "slug", "content")
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "published_at"
    ordering = ("-published_at", "-created_at")
    autocomplete_fields = ("author", "category")
    readonly_fields = ("created_at", "updated_at")

    formfield_overrides = {
        models.TextField: {"widget": WysiwygWidget}
    }
