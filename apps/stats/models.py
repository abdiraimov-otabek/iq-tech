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
