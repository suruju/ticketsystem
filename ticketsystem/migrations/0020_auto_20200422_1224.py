# Generated by Django 3.0.5 on 2020-04-22 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticketsystem', '0019_auto_20200421_1859'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ChildModel',
        ),
        migrations.DeleteModel(
            name='ParentModel',
        ),
    ]
