from django.db import models

from apps.team.models import TeamMember
from apps.technology.models import Technology
class ProjectCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    STATUS_CHOICES = [
        ("planning", "Planning"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
        ("archived", "Archived"),
    ]

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE, related_name="project_categories", null=True, blank=True)
    image = models.ImageField(upload_to="projects/images/", blank=True, null=True)
    demo_url = models.URLField(max_length=300, blank=True)
    tech_stack = models.ManyToManyField(Technology, blank=True)
    team = models.ManyToManyField(TeamMember, related_name="projects", blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="planning")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
