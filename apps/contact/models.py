from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=70)
    phone_number = models.CharField(max_length=15)
    request = models.TextField(max_length=300)

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
        ordering = ["-id"]

    def __str__(self):
        return f"{self.name} ({self.phone_number})"
