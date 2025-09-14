from django.apps import AppConfig
from django.utils.module_loading import autodiscover_modules


class PartnersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.partners'

    def ready(self):
        autodiscover_modules('translation')
