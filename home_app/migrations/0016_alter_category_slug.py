# Generated by Django 5.0.8 on 2024-08-08 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0015_auto_20210904_0235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, help_text='URL que tendrá la categoría', null=True, unique=True),
        ),
    ]
