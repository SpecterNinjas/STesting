from django.contrib import admin

from .models import Publications


class PublicationAdmin(admin.ModelAdmin):
    list_display = ['title', 'pub_type', 'file', 'created', 'updated']
    list_filter = ['title', 'pub_type', 'created']


admin.site.register(Publications, PublicationAdmin)
