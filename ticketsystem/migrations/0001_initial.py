# Generated by Django 3.0.5 on 2020-04-13 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('category',),
            },
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ammenities', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'facility',
                'verbose_name_plural': 'facilities',
                'ordering': ('ammenities',),
            },
        ),
        migrations.CreateModel(
            name='RouteDestination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destinationlocation', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'route',
                'verbose_name_plural': 'routes',
                'ordering': ('destinationlocation',),
            },
        ),
        migrations.CreateModel(
            name='VehicleCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(db_index=True, max_length=100)),
                ('address', models.CharField(db_index=True, max_length=200)),
                ('company_info', models.TextField(blank=True)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('account_status', models.CharField(choices=[('Active', 'Active'), ('Pending', 'Pending'), ('Deactivated', 'Deactivated')], max_length=20)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'company',
                'verbose_name_plural': 'companies',
                'ordering': ('company_name',),
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_name', models.CharField(db_index=True, max_length=100, null=True)),
                ('vehicle_number', models.CharField(max_length=20, null=True)),
                ('departurefrom', models.CharField(max_length=100, null=True)),
                ('departureto', models.CharField(max_length=100, null=True)),
                ('departuretime', models.TimeField()),
                ('seatplan', models.CharField(max_length=50, null=True)),
                ('seatcapacity', models.PositiveIntegerField(null=True, verbose_name=2)),
                ('ticketprice', models.PositiveIntegerField(verbose_name=4)),
                ('vehicle_photo', models.ImageField(blank=True, upload_to='')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('boardingpointone', models.CharField(max_length=200, null=True)),
                ('boardingpointtwo', models.CharField(max_length=200, null=True)),
                ('boardingpointthree', models.CharField(max_length=200, null=True)),
                ('dropoffpointone', models.CharField(max_length=200, null=True)),
                ('dropoffpointtwo', models.CharField(max_length=200, null=True)),
                ('dropoffpointthree', models.CharField(max_length=200, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vehiclecategory', to='ticketsystem.Category')),
                ('facility', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vehiclefacility', to='ticketsystem.Facility')),
                ('vehicleowner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='company', to='ticketsystem.VehicleCompany')),
            ],
            options={
                'ordering': ('vehicle_name',),
                'index_together': {('id', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(db_index=True, max_length=100)),
                ('address', models.CharField(db_index=True, max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('departurefrom', models.CharField(max_length=100, null=True)),
                ('departureto', models.CharField(max_length=100, null=True)),
                ('departuredate', models.DateField()),
                ('departuretime', models.TimeField()),
                ('seatnumber', models.CharField(max_length=50)),
                ('totalprice', models.PositiveIntegerField()),
                ('paymentmode', models.CharField(choices=[('Online Payment', 'Online Payment'), ('Offline Payment', 'Offline Payment')], max_length=50)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('busid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bus', to='ticketsystem.Vehicle')),
            ],
            options={
                'ordering': ('-departuredate',),
            },
        ),
    ]
