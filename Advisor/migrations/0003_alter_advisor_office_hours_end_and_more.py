# Generated by Django 5.0.6 on 2024-05-26 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Advisor', '0002_advisor_email_advisor_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advisor',
            name='office_hours_end',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='advisor',
            name='office_hours_start',
            field=models.TimeField(null=True),
        ),
    ]