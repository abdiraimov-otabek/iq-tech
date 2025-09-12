from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import WysiwygWidget
from django.contrib import admin
from .models import BlogCategory, BlogPost


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group

from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from unfold.admin import ModelAdmin


admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    # Forms loaded from `unfold.forms`
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass


@admin.register(BlogCategory)
class BlogCategoryAdmin(ModelAdmin):
    list_display = ("name", "slug", "description", "created_at")
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("name",)


@admin.register(BlogPost)
class BlogPostAdmin(ModelAdmin):
    list_display = (
        "title_uz",
        "author",
        "category",
        "status",
        "is_featured",
        "published_at",
        "created_at",
    )
    list_filter = ("status", "is_featured", "category", "author")
    search_fields = ("title_uz", "slug", "content")
    prepopulated_fields = {"slug": ("title_uz",)}
    date_hierarchy = "published_at"
    ordering = ("-published_at", "-created_at")
    autocomplete_fields = ("author", "category")
    readonly_fields = ("created_at", "updated_at")

    formfield_overrides = {
        BlogPost._meta.get_field("content").__class__: {"widget": WysiwygWidget},
    }
