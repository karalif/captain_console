# Generated by Django 3.0.6 on 2020-05-15 17:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payment', '0006_auto_20200515_1748'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('card_number', models.CharField(max_length=255)),
                ('exp_month', models.DecimalField(decimal_places=0, max_digits=2)),
                ('exp_year', models.DecimalField(decimal_places=0, max_digits=2)),
                ('cvv', models.DecimalField(decimal_places=0, max_digits=3)),
                ('active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]