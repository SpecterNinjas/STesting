# Generated by Django 2.2.19 on 2021-04-09 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='title_en',
            field=models.CharField(max_length=700, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='title_ru',
            field=models.CharField(max_length=700, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='title_uz',
            field=models.CharField(max_length=700, null=True),
        ),
    ]
