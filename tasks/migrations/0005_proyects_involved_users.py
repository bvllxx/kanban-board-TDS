# Generated by Django 4.1 on 2023-12-12 14:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0004_alter_proyects_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyects',
            name='involved_users',
            field=models.ManyToManyField(blank=True, related_name='proyects', to=settings.AUTH_USER_MODEL),
        ),
    ]
