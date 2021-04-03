# Generated by Django 2.2.5 on 2021-04-02 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=700)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=13)),
                ('company_description', models.TextField()),
                ('instagram', models.URLField()),
                ('telegram', models.URLField()),
                ('facebook', models.URLField()),
                ('twitter', models.URLField()),
            ],
        ),
    ]