# Generated by Django 3.0.6 on 2020-05-15 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_auto_20200515_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='billing_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='payment.BillingInfo'),
        ),
    ]
