from modeltranslation.translator import TranslationOptions, register
from .models import Role, TeamMember

@register(Role)
class RoleTranslationOptions(TranslationOptions):
    fields = (
        "name",
    )

@register(TeamMember)
class TeamMemberTranslationOptions(TranslationOptions):
    fields = (
        "first_name",
        "last_name",
        "bio"
    )