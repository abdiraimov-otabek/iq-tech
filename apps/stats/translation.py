from modeltranslation.translator import TranslationOptions, register
from .models import Reviews

@register(Reviews)
class ReviewsTranslationOptions(TranslationOptions):
    fields = (
        "name",
        "content"
    )