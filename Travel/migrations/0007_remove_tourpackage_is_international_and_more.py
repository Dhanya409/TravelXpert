# Generated by Django 5.1.5 on 2025-01-20 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Travel', '0006_tourpackage_is_international_passportdetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tourpackage',
            name='is_international',
        ),
        migrations.DeleteModel(
            name='PassportDetails',
        ),
    ]
