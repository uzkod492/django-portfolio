# Generated by Django 4.1.4 on 2022-12-22 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0006_user_social'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
