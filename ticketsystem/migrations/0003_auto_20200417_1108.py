# Generated by Django 3.0.5 on 2020-04-17 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketsystem', '0002_auto_20200417_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='seatcapacity',
            field=models.PositiveIntegerField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='ticketprice',
            field=models.PositiveIntegerField(max_length=4),
        ),
    ]
