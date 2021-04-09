from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Publications


class PublicationAdmin(TranslationAdmin):
    list_display = ['title', 'pub_type', 'file', 'created', 'updated']
    list_filter = ['title', 'pub_type', 'created']


admin.site.register(Publications, PublicationAdmin)
