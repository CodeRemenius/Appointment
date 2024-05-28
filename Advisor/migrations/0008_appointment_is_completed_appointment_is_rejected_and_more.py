# Generated by Django 5.0.6 on 2024-05-26 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Advisor', '0007_task_failed'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='appointment',
            name='is_rejected',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='appointment',
            name='mode_of_meeting',
            field=models.CharField(choices=[('Online', 'Online'), ('Physical', 'Physical')], default='', max_length=50),
        ),
    ]
