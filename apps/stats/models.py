from django.db import models


class Statistics(models.Model):
    total_projects = models.PositiveIntegerField(default=0)
    total_clients = models.PositiveIntegerField(default=0)
    years_experience = models.PositiveIntegerField(default=0)
    team_members = models.PositiveIntegerField(default=0)
    happy_customers = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Statistics"
        verbose_name_plural = "Statistics"

    def __str__(self):
        return f"Statistics"

class Reviews(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "review"
        verbose_name_plural = "reviews"