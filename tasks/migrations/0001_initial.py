# Generated by Django 4.1 on 2023-12-19 19:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Proyects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('begin_date', models.DateField(auto_now_add=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('founding_src_name', models.CharField(default='N/A', max_length=30)),
                ('founding_src', models.CharField(choices=[('interna', 'Interna'), ('externa', 'Externa')], default='interna', max_length=10)),
                ('status', models.CharField(choices=[('pendiente', 'Pendiente'), ('en_proceso', 'En Proceso'), ('finalizado', 'Finalizado')], default='pendiente', max_length=20)),
                ('involved_users', models.ManyToManyField(blank=True, related_name='proyects', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
