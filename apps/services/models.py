from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.CharField(max_length=200, blank=True)
    icon = models.FileField(upload_to="services/icons/", blank=True, null=True)
    file = models.FileField(upload_to="services/3d_file/", blank=True, null=True)
    colors = models.CharField(max_length=7, default="#000000")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.title
