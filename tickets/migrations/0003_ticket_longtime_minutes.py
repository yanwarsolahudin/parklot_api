# Generated by Django 3.0.1 on 2020-01-05 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_ticket_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='longtime_minutes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
