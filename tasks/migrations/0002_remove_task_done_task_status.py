# Generated by Django 4.1 on 2023-11-12 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='done',
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('en_proceso', 'En Proceso'), ('finalizado', 'Finalizado')], default='pendiente', max_length=20),
        ),
    ]