from modeltranslation.translator import TranslationOptions, register
from .models import Technology

@register(Technology)
class TechnologyTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )