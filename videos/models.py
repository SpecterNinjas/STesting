from django.db import models
from django.utils.translation import ugettext_lazy as _


class Video(models.Model):
    ASSESSMENT_TYPES = (
        ('TIMSS', _('TIMSS')),
        ('PISA', _('PISA')),
        ('PIRLS', _('PIRLS')),
    )
    VIDEO_TYPES = (
        ('teachers', _('teachers')),
        ('students', _('students')),
        ('parents', _('parents')),
    )

    title = models.CharField(max_length=700)
    watch_count = models.PositiveIntegerField(default=0)
    assessment_type = models.CharField(max_length=20, choices=ASSESSMENT_TYPES)
    video_type = models.CharField(max_length=20, choices=VIDEO_TYPES)
    video = models.FileField(upload_to='publications/videos/')

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = _('Video')
        verbose_name_plural = _('Videos')
