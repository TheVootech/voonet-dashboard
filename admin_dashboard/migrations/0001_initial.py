# Generated by Django 4.2.2 on 2025-01-20 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booked_date', models.DateField(auto_now_add=True)),
                ('booked_by', models.CharField(default='mujeeb', max_length=100)),
                ('booking_id', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False)),
                ('payment_ref_no', models.CharField(max_length=50)),
                ('payment_status', models.CharField(choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')], max_length=20)),
                ('grand_total', models.FloatField(default=0)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=30, unique=True)),
                ('no_of_adult', models.BooleanField(default=True)),
                ('no_of_child', models.BooleanField(default=True)),
                ('no_of_infant', models.BooleanField(default=True)),
                ('rate_of_adult', models.BooleanField(default=True)),
                ('rate_of_child', models.BooleanField(default=True)),
                ('rate_of_infant', models.BooleanField(default=True)),
                ('pickup_location', models.BooleanField(default=True)),
                ('drop_location', models.BooleanField(default=True)),
                ('room_no', models.BooleanField(default=True)),
                ('remark', models.BooleanField(default=True)),
                ('date', models.BooleanField(default=True)),
                ('time', models.BooleanField(default=True)),
                ('pickup_time', models.BooleanField(default=True)),
                ('transfer_type', models.BooleanField(default=True)),
                ('vehicle_type', models.BooleanField(default=True)),
                ('vehicle_name', models.BooleanField(default=True)),
                ('no_of_luggage', models.BooleanField(default=True)),
                ('flight_time', models.BooleanField(default=True)),
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
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Company_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('language_id', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False)),
                ('language_name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('package_id', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False)),
                ('package_code', models.CharField(max_length=20)),
                ('package_title', models.CharField(max_length=30)),
                ('package_city', models.CharField(max_length=30)),
                ('web_id', models.CharField(max_length=200)),
                ('web_sku', models.CharField(max_length=200)),
                ('website_link', models.CharField(max_length=300)),
                ('short_description', models.TextField(max_length=300)),
                ('highlights', models.TextField(max_length=300)),
                ('description', models.TextField(max_length=1000)),
                ('inclusions', models.CharField(max_length=500)),
                ('exclusions', models.CharField(max_length=500)),
                ('transportation', models.CharField(choices=[('Sharing', 'Sharing'), ('Private', 'Private'), ('Without Transfer', 'Without Transfer'), ('Tickets Only', 'Tickets Only')], max_length=30)),
                ('open_hours', models.CharField(max_length=30)),
                ('sunday', models.BooleanField(blank=True, default=True, null=True)),
                ('monday', models.BooleanField(blank=True, default=True, null=True)),
                ('tuesday', models.BooleanField(blank=True, default=True, null=True)),
                ('wednesday', models.BooleanField(blank=True, default=True, null=True)),
                ('thursday', models.BooleanField(blank=True, default=True, null=True)),
                ('friday', models.BooleanField(blank=True, default=True, null=True)),
                ('saturday', models.BooleanField(blank=True, default=True, null=True)),
                ('location', models.CharField(max_length=100)),
                ('adult_rate', models.CharField(max_length=20)),
                ('child_rate', models.CharField(max_length=20)),
                ('infant_rate', models.CharField(max_length=20)),
                ('adult_age', models.CharField(max_length=10)),
                ('child_age', models.CharField(max_length=10)),
                ('infant_age', models.CharField(max_length=10)),
                ('image_link', models.CharField(max_length=600)),
                ('video_link', models.CharField(max_length=600)),
                ('is_deleted', models.BooleanField(default=False)),
                ('language', models.ManyToManyField(to='admin_dashboard.language')),
                ('package_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_dashboard.category')),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Payment_mode',
            fields=[
                ('payment_id', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False)),
                ('payment_mode', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('reminder_id', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=200, unique=True)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('status', models.CharField(default='Active', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Status_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_dashboard.package')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('supplier_id', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('tl_number', models.CharField(max_length=100)),
                ('vat_number', models.CharField(max_length=100)),
                ('address1', models.CharField(max_length=100)),
                ('city1', models.CharField(max_length=100)),
                ('state1', models.CharField(max_length=100)),
                ('country1', models.CharField(max_length=100)),
                ('pincode1', models.CharField(max_length=100)),
                ('phone1', models.PositiveIntegerField()),
                ('address2', models.CharField(blank=True, max_length=100, null=True)),
                ('city2', models.CharField(blank=True, max_length=100, null=True)),
                ('state2', models.CharField(blank=True, max_length=100, null=True)),
                ('country2', models.CharField(blank=True, max_length=100, null=True)),
                ('pincode2', models.CharField(blank=True, max_length=100, null=True)),
                ('phone2', models.PositiveIntegerField(blank=True, null=True)),
                ('mobile', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('trade_license', models.FileField(upload_to='trade_license/')),
                ('vat_certificate', models.FileField(upload_to='vat_certificate/')),
                ('account_name', models.CharField(max_length=200)),
                ('bank_name', models.CharField(max_length=200)),
                ('account_number', models.CharField(max_length=100)),
                ('iban', models.CharField(max_length=200)),
                ('swift', models.CharField(max_length=200)),
                ('routing_number', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=200)),
                ('is_deleted', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_dashboard.category')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_dashboard.status_type')),
                ('supplier_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_dashboard.supplier_type')),
            ],
        ),
        migrations.CreateModel(
            name='Package_images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='package_images/')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_dashboard.package')),
            ],
        ),
        migrations.AddField(
            model_name='package',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_dashboard.status_type'),
        ),
        migrations.CreateModel(
            name='Hero_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='Hero_images/')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_dashboard.package')),
            ],
        ),
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
                ('is_deleted', models.BooleanField(default=False)),
                ('language', models.ManyToManyField(to='admin_dashboard.language')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_dashboard.status_type')),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('driver_id', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('driver_type', models.CharField(choices=[('Limousine', 'Limousine'), ('Transportation', 'Transportation'), ('Tourism', 'Tourism'), ('Stretch limo', 'Stretch limo')], max_length=100)),
                ('vehicle_make', models.CharField(max_length=100)),
                ('vehicle_brand', models.CharField(max_length=100)),
                ('vehicle_year', models.CharField(max_length=10)),
                ('mobile1', models.PositiveIntegerField()),
                ('mobile2', models.PositiveIntegerField()),
                ('whatsapp1', models.PositiveIntegerField()),
                ('whatsapp2', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('vehicle_registration', models.CharField(max_length=100)),
                ('rc_expiry', models.DateField()),
                ('dl_number', models.CharField(max_length=100)),
                ('dl_expiry', models.DateField()),
                ('passport_number', models.CharField(max_length=100)),
                ('passport_expiry', models.DateField()),
                ('emirates_id_number', models.CharField(max_length=100)),
                ('emirates_id_expiry', models.DateField()),
                ('visa_number', models.CharField(max_length=100)),
                ('visa_expiry', models.DateField()),
                ('vehicle_rc', models.FileField(upload_to='driver_vehicle_rc/')),
                ('insurance', models.FileField(upload_to='driver_vehicle_insurance/')),
                ('driving_license', models.FileField(upload_to='driving_license/')),
                ('passport', models.FileField(upload_to='driver_passport/')),
                ('emirates_id', models.FileField(upload_to='driver_emirates_id/')),
                ('visa', models.FileField(upload_to='driver_visa/')),
                ('photos', models.FileField(upload_to='driver_photos/')),
                ('is_deleted', models.BooleanField(default=False)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_dashboard.status_type')),
            ],
        ),
        migrations.CreateModel(
            name='Contact_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('designation', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile', models.PositiveIntegerField(blank=True, null=True)),
                ('whatsapp', models.PositiveIntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_dashboard.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='Company_contact_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('designation', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile', models.PositiveIntegerField(blank=True, null=True)),
                ('whatsapp', models.PositiveIntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_dashboard.company')),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='company_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_dashboard.company_type'),
        ),
        migrations.AddField(
            model_name='company',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_dashboard.status_type'),
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to='admin_dashboard.parent')),
            ],
        ),
        migrations.CreateModel(
            name='Booking_Trip_details',
            fields=[
                ('guest_name', models.CharField(max_length=200)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('contact_number', models.CharField(max_length=20)),
                ('whatsapp_number', models.CharField(blank=True, max_length=20, null=True)),
                ('booking_trip_id', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False)),
                ('trip_date', models.DateField()),
                ('trip_time', models.TimeField()),
                ('no_of_adult', models.PositiveIntegerField()),
                ('no_of_child', models.PositiveIntegerField()),
                ('no_of_infant', models.PositiveIntegerField()),
                ('rate_of_adult', models.PositiveIntegerField()),
                ('rate_of_child', models.PositiveIntegerField()),
                ('rate_of_infant', models.PositiveIntegerField()),
                ('pickup_location', models.CharField(blank=True, max_length=100, null=True)),
                ('drop_location', models.CharField(blank=True, max_length=100, null=True)),
                ('room_no', models.CharField(blank=True, max_length=100, null=True)),
                ('pickup_time', models.TimeField(blank=True, null=True)),
                ('transfer_type', models.CharField(blank=True, max_length=100, null=True)),
                ('vehicle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('no_of_luggage', models.PositiveIntegerField(blank=True, null=True)),
                ('flight_time', models.TimeField(blank=True, null=True)),
                ('remark', models.CharField(blank=True, max_length=500, null=True)),
                ('total_amount', models.FloatField(default=0)),
                ('vat', models.FloatField(default=5)),
                ('vat_amount', models.FloatField(default=0)),
                ('grand_total', models.FloatField(default=0)),
                ('exclude', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookingtripdetails', to='admin_dashboard.booking')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_dashboard.category')),
                ('driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_dashboard.driver')),
                ('guide', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_dashboard.guide')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_dashboard.package')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_dashboard.supplier')),
                ('vehicle_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_dashboard.vehicle_type')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_dashboard.company'),
        ),
        migrations.AddField(
            model_name='booking',
            name='contact_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_dashboard.company_contact_details'),
        ),
        migrations.AddField(
            model_name='booking',
            name='payment_mode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_dashboard.payment_mode'),
        ),
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_dashboard.status_type'),
        ),
        migrations.CreateModel(
            name='Supplier_allocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adultprice', models.PositiveIntegerField()),
                ('childprice', models.PositiveIntegerField()),
                ('infantprice', models.PositiveIntegerField()),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_dashboard.package')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_dashboard.supplier')),
            ],
            options={
                'unique_together': {('package', 'supplier')},
            },
        ),
    ]
