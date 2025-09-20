from django.db import models
from django.utils.text import slugify


class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Role"
        verbose_name_plural = "Roles"
        ordering = ["name"]

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    full_name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    role = models.ManyToManyField(
        Role, related_name="team_members"
    )
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to="team/photos/", blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"
        ordering = ["-created_at"]

    def __str__(self):
        return self.full_name