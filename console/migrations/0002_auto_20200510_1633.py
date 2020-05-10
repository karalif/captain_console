# Generated by Django 3.0.6 on 2020-05-10 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('console', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='console',
            name='image',
        ),
        migrations.CreateModel(
            name='GameImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=999)),
                ('console', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='console.Console')),
            ],
        ),
    ]
