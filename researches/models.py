from django.db import models


class Research(models.Model):

    PUB_TYPES = (
        ('international', 'international'),
        ('national', 'national'),
    )

    title = models.CharField(max_length=700)
    description = models.TextField()
    image = models.ImageField(upload_to='publications/researches/')
    research_type = models.CharField(max_length=20, choices=PUB_TYPES)
    watch_count = models.PositiveIntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Research'
        verbose_name_plural = 'Researches'

