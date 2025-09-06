from modeltranslation.translator import TranslationOptions, register
from .models import BlogPost, BlogCategory

@register(BlogCategory)
class BloCategoryTranslationOptions(TranslationOptions):
    fields = (
        "name",
        "description"
    )

@register(BlogPost)
class BlogPostTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "content"
    )