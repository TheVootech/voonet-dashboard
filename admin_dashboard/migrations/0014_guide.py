# Generated by Django 4.2.2 on 2024-12-18 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0013_driver'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('guide_id', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('abudhabi_license', models.BooleanField(default=True)),
                ('dubai_license', models.BooleanField(default=True)),
                ('rak_license', models.BooleanField(default=True)),
                ('sharjah_license', models.BooleanField(default=True)),
                ('fujairah_license', models.BooleanField(default=True)),
                ('mobile1', models.PositiveIntegerField()),
                ('mobile2', models.PositiveIntegerField()),
                ('whatsapp1', models.PositiveIntegerField()),
                ('whatsapp2', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('license_number', models.CharField(max_length=100)),
                ('license_expiry', models.DateField()),
                ('passport_number', models.CharField(max_length=100)),
                ('passport_expiry', models.DateField()),
                ('emirates_id_number', models.CharField(max_length=100)),
                ('emirates_id_expiry', models.DateField()),
                ('visa_number', models.CharField(max_length=100)),
                ('visa_expiry', models.DateField()),
                ('license_copy', models.FileField(upload_to='guide_license/')),
                ('passport', models.FileField(upload_to='guide_passport/')),
                ('emirates_id', models.FileField(upload_to='guide_emirates_id/')),
                ('visa', models.FileField(upload_to='guide_visa/')),
                ('photos', models.FileField(upload_to='driver_photos/')),
                ('language', models.ManyToManyField(to='admin_dashboard.language')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_dashboard.status_type')),
            ],
        ),
    ]