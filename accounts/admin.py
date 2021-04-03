from django.contrib import admin

from .models import ProfileCreation


class ProfileCreationAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'login', 'phone', 'area', 'city', 'school', 'grade', 'created', 'updated']
    list_filter = ('fullname', 'created')


admin.site.register(ProfileCreation, ProfileCreationAdmin)
