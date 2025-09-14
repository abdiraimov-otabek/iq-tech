from django.db import models

class Partner(models.Model):
    name = models.CharField(max_length=100)
    logo = models.FileField(upload_to="partners/logos/")
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Partner"
        verbose_name_plural = "Partners"