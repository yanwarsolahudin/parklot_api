# Generated by Django 3.0.1 on 2020-01-04 07:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('floors', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('slot_type', models.CharField(choices=[('compact', 'Compact'), ('large', 'Large'), ('handicapped', 'Handicapped'), ('motorcycle', 'Motorcycle')], default='large', max_length=12)),
                ('status', models.CharField(choices=[('filled', 'Filled'), ('available', 'Available')], default='available', max_length=9)),
                ('stage', models.BooleanField(default=True)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adminslots', to=settings.AUTH_USER_MODEL)),
                ('floor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='floorslots', to='floors.Floor')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
