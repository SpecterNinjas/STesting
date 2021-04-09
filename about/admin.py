from django.contrib import admin
from .models import About
from modeltranslation.admin import TranslationAdmin


class AboutAdmin(TranslationAdmin):
    list_display = ['email', 'phone', 'address']


admin.site.register(About, AboutAdmin)
