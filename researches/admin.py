from django.contrib import admin
from .models import Research
from modeltranslation.admin import TranslationAdmin


class ResearchAdmin(TranslationAdmin):
    list_display = ['title', 'research_type', 'watch_count', 'created']
    list_filter = ['title', 'research_type', 'created']


admin.site.register(Research, ResearchAdmin)
