from django.db import models

from apps.team.models import TeamMember


class BlogCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(max_length=64, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Blog Category"
        verbose_name_plural = "Blog Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
        ("archived", "Archived"),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        TeamMember, on_delete=models.CASCADE, related_name="blog_posts"
    )
    category = models.ForeignKey(
        BlogCategory, on_delete=models.SET_NULL, null=True, related_name="posts"
    )
    content = models.TextField()
    cover_image = models.ImageField(upload_to="blog/covers/", blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")
    is_featured = models.BooleanField(default=False)
    published_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
        ordering = ["-published_at", "-created_at"]

    def __str__(self):
        return self.title

    def is_published(self):
        return self.status == "published" and self.published_at is not None
