# Generated by Django 3.0.1 on 2021-09-04 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services_app', '0002_auto_20210903_0349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='services',
            old_name='category_id',
            new_name='category',
        ),
    ]
