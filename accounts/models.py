from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class ProfileCreation(models.Model):
    AREAS = (
        ('', _('Hududingizni tanlang')),
        ('hudud1', _('hudud1')),
        ('hudud2', _('hudud2')),
        ('hudud3', _('hudud3')),
    )
    CITIES = (
        ('', _('Shahar/tumaningizni tanlang')),
        ('Buxoro', _('Buxoro')),
        ('Toshkent', _('Toshkent')),
        ('Samarqand', _('Samarqand')),
    )
    SCHOOLS = (
        ('', _('Maktabingizni tanlang')),
        ('maktab1', _('maktab1')),
        ('maktab2', _('maktab2')),
        ('maktab3', _('maktab3')),

    )
    GRADES = (
        ('', _('Sinfingizni tanlang')),
        ('sinf1', _('sinf1')),
        ('sinf2', _('sinf2')),
        ('sinf3', _('sinf3')),
    )
    fullname = models.CharField(max_length=100)
    login = models.CharField(max_length=100, blank=True, null=True)  # assigning User->username
    phone = models.CharField(max_length=13, unique=True)
    area = models.CharField(max_length=50, choices=AREAS)
    city = models.CharField(max_length=50, choices=CITIES)
    school = models.CharField(max_length=50, choices=SCHOOLS)
    grade = models.CharField(max_length=50, choices=GRADES)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.fullname)

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')
