# Generated by Django 4.1.4 on 2022-12-22 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_category_project_imagelist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='image',
        ),
    ]
