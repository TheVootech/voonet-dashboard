# Generated by Django 4.2.2 on 2024-12-27 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='booking_trip_details',
            name='drop_location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='booking_trip_details',
            name='flight_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='booking_trip_details',
            name='no_of_luggage',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='booking_trip_details',
            name='pickup_location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='booking_trip_details',
            name='pickup_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='booking_trip_details',
            name='remark',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='booking_trip_details',
            name='room_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='booking_trip_details',
            name='transfer_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='booking_trip_details',
            name='vehicle_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='booking_trip_details',
            name='vehicle_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_dashboard.vehicle_type'),
        ),
    ]