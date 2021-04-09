from django.contrib import admin
from .models import Video
from modeltranslation.admin import TranslationAdmin


class VideoAdmin(TranslationAdmin):
    list_display = ['title', 'assessment_type', 'video_type', 'watch_count', 'created']
    list_filter = ['title', 'video_type', 'assessment_type', 'created']


admin.site.register(Video, VideoAdmin)
