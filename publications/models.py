from django.db import models
from django.utils.translation import ugettext_lazy as _


class Publications(models.Model):
    PUB_TYPES = (
        ('international', _('international')),
        ('national', _('national')),
    )

    title = models.CharField(max_length=700)
    description = models.TextField()
    image = models.ImageField(upload_to='publications/images/', blank=True, null=True)
    pub_type = models.CharField(max_length=20, choices=PUB_TYPES)
    file = models.FileField(upload_to='publications/files/')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = _('Publication')
        verbose_name_plural = _('Publications')
