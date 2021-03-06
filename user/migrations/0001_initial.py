# Generated by Django 3.0.6 on 2020-05-13 13:02

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=99)),
                ('birth_date', models.DateField(default=datetime.date.today)),
                ('address', models.CharField(blank=True, max_length=999)),
                ('zip_code', models.CharField(blank=True, max_length=999)),
                ('city', models.CharField(blank=True, max_length=999)),
                ('country', models.CharField(blank=True, max_length=999)),
                ('profile_image', models.CharField(blank=True, max_length=9999)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
