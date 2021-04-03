from django.db import models
from django.contrib.auth.models import User


class ProfileCreation(models.Model):
    AREAS = (
        ('', 'Hududingizni tanlang'),
        ('hudud1', 'hudud1'),
        ('hudud2', 'hudud2'),
        ('hudud3', 'hudud3'),
    )
    CITIES = (
        ('', 'Shahar/tumaningizni tanlang'),
        ('Buxoro', 'Buxoro'),
        ('Toshkent', 'Toshkent'),
        ('Samarqand', 'Samarqand'),
    )
    SCHOOLS = (
        ('', 'Maktabingizni tanlang'),
        ('maktab1', 'maktab1'),
        ('maktab2', 'maktab2'),
        ('maktab3', 'maktab3'),

    )
    GRADES = (
        ('', 'Sinfingizni tanlang'),
        ('sinf1', 'sinf1'),
        ('sinf2', 'sinf2'),
        ('sinf3', 'sinf3'),
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
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
