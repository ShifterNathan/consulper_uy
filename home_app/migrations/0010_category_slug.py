# Generated by Django 3.0.1 on 2021-09-04 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0009_delete_services'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
