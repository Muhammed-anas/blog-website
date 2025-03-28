# Generated by Django 5.1.7 on 2025-03-19 06:23

import django.db.models.deletion
import localflavor.us.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(blank=True, max_length=100)),
                ('address2', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(blank=True, max_length=30)),
                ('state', localflavor.us.models.USStateField(default='NY', max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.location'),
        ),
    ]
