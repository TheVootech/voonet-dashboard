# Generated by Django 4.2.2 on 2024-11-29 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0008_parent_child'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('tl_number', models.PositiveIntegerField()),
                ('vat_number', models.PositiveIntegerField()),
                ('address1', models.CharField(max_length=100)),
                ('city1', models.CharField(max_length=100)),
                ('state1', models.CharField(max_length=100)),
                ('country1', models.CharField(max_length=100)),
                ('pincode1', models.PositiveIntegerField()),
                ('phone1', models.PositiveIntegerField()),
                ('address2', models.CharField(blank=True, max_length=100, null=True)),
                ('city2', models.CharField(blank=True, max_length=100, null=True)),
                ('state2', models.CharField(blank=True, max_length=100, null=True)),
                ('country2', models.CharField(blank=True, max_length=100, null=True)),
                ('pincode2', models.PositiveIntegerField(blank=True, null=True)),
                ('phone2', models.PositiveIntegerField(blank=True, null=True)),
                ('mobile', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('trade_license', models.FileField(upload_to='company_trade_license/')),
                ('vat_certificate', models.FileField(upload_to='company_vat_cerificate/')),
                ('account_name', models.CharField(max_length=200)),
                ('bank_name', models.CharField(max_length=200)),
                ('account_number', models.PositiveIntegerField()),
                ('iban', models.CharField(max_length=200)),
                ('swift', models.CharField(max_length=200)),
                ('routing_number', models.PositiveIntegerField()),
                ('branch', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=200)),
                ('company_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_dashboard.company_type')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_dashboard.status_type')),
            ],
        ),
    ]