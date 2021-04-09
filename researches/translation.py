from .models import Research
from modeltranslation.translator import register, TranslationOptions


@register(Research)
class AboutTranslationOptions(TranslationOptions):
    fields = ['title', 'description']
