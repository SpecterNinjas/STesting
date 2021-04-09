from modeltranslation.translator import register, TranslationOptions
from .models import Publications


@register(Publications)
class PublicationsTranslationOptions(TranslationOptions):
    fields = ['title', 'description', ]
