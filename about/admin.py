from django.contrib import admin
from .models import About


class AboutAdmin(admin.ModelAdmin):
    list_display = ['email', 'phone', 'address']


admin.site.register(About, AboutAdmin)
