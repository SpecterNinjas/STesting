from django.db import models


class About(models.Model):
    address = models.CharField(max_length=700)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=13)
    company_description = models.TextField(max_length=3000)

    # social apps
    instagram = models.URLField(max_length=200)
    telegram = models.URLField(max_length=200)
    facebook = models.URLField(max_length=200)
    twitter = models.URLField(max_length=200)

    class Meta:
        verbose_name = 'Company Details'
        verbose_name_plural = 'Company Details'
