# Generated by Django 3.2.5 on 2021-07-21 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mozio_app', '0003_alter_provider_point'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='provider',
            name='point',
        ),
    ]