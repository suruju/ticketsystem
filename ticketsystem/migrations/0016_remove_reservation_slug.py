# Generated by Django 3.0.5 on 2020-04-20 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticketsystem', '0015_auto_20200420_1757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='slug',
        ),
    ]
