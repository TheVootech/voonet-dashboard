from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe

# Create your models here.

class Status_type(models.Model):
    status=models.CharField(max_length=100,unique=True)
    
    def __str__(self):
        return self.status
    
    

class Language(models.Model):
    # Custom ID starts with 'LAN' followed by an auto-incrementing number
    language_id = models.CharField(max_length=10, primary_key=True, editable=False)
    language_name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.language_name

    def save(self, *args, **kwargs):
        if not self.language_id:  # Only generate ID if it's not already set
            # Get the last language added to calculate the next ID
            last_language = Language.objects.order_by('language_id').last()
            if last_language:
                # Extract the number part and increment it
                last_id_number = int(last_language.language_id[3:])  # Skip 'LAN' prefix
                next_id_number = last_id_number + 1
                # Ensure the ID has 2 digits for padding (e.g., LAN01, LAN02, ...)
                self.language_id = f"LAN{next_id_number:02d}"  # 2 digits for padding
            else:
                # If no languages exist, start with 'LAN01'
                self.language_id = 'LAN01'

        super(Language, self).save(*args, **kwargs)


    



class Category(models.Model):
    category_id=models.CharField(max_length=10, primary_key=True, editable=False)
    category_name=models.CharField(max_length=30,unique=True)
    no_of_adult=models.BooleanField(default=True)
    no_of_child=models.BooleanField(default=True)
    no_of_infant=models.BooleanField(default=True)
    rate_of_adult=models.BooleanField(default=True)
    rate_of_child=models.BooleanField(default=True)
    rate_of_infant=models.BooleanField(default=True)
    pickup_location=models.BooleanField(default=True)
    drop_location=models.BooleanField(default=True)
    room_no=models.BooleanField(default=True)
    remark=models.BooleanField(default=True)
    date=models.BooleanField(default=True)
    time=models.BooleanField(default=True)
    pickup_time=models.BooleanField(default=True)
    transfer_type=models.BooleanField(default=True)
    vehicle_type=models.BooleanField(default=True)
    vehicle_name=models.BooleanField(default=True)
    no_of_luggage=models.BooleanField(default=True)
    flight_time=models.BooleanField(default=True)

    
    def __str__(self):
        return self.category_name
    
    def save(self, *args, **kwargs):
        if not self.category_id:  # Only generate ID if it's not already set
            # Get the last language added to calculate the next ID
            last_category = Category.objects.order_by('category_id').last()
            if last_category:
                # Extract the number part and increment it
                last_id_number = int(last_category.category_id[3:])  # Skip 'LAN' prefix
                next_id_number = last_id_number + 1
                # Ensure the ID has 2 digits for padding (e.g., LAN01, LAN02, ...)
                self.category_id = f"CAT{next_id_number:02d}"  # 2 digits for padding
            else:
                # If no languages exist, start with 'LAN01'
                self.category_id = 'CAT01'

        super(Category, self).save(*args, **kwargs)



    
    
class Supplier_type(models.Model):
    type_name=models.CharField(max_length=100,unique=True)
    
    def __str__(self):
        return self.type_name
    
class Company_type(models.Model):
    type_name=models.CharField(max_length=100,unique=True)
    
    def __str__(self):
        return self.type_name
    

    
    
class Supplier(models.Model):
    supplier_id=models.CharField(max_length=10,primary_key=True,editable=False)
    name=models.CharField(max_length=100)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    supplier_type=models.ForeignKey(Supplier_type,on_delete=models.CASCADE)
    tl_number=models.CharField(max_length=100)
    vat_number=models.CharField(max_length=100)
    address1=models.CharField(max_length=100)
    city1=models.CharField(max_length=100)
    state1=models.CharField(max_length=100)
    country1=models.CharField(max_length=100)
    pincode1=models.CharField(max_length=100)
    phone1=models.PositiveIntegerField()
    address2=models.CharField(max_length=100,blank=True,null=True)
    city2=models.CharField(max_length=100,blank=True,null=True)
    state2=models.CharField(max_length=100,blank=True,null=True)
    country2=models.CharField(max_length=100,blank=True,null=True)
    pincode2=models.CharField(max_length=100,blank=True,null=True)
    phone2=models.PositiveIntegerField(blank=True,null=True)
    mobile=models.PositiveIntegerField()
    email=models.EmailField()
    trade_license=models.FileField(upload_to='trade_license/')
    vat_certificate=models.FileField(upload_to='vat_certificate/')
    account_name=models.CharField(max_length=200)
    bank_name=models.CharField(max_length=200)
    account_number=models.CharField(max_length=100)
    iban=models.CharField(max_length=200)
    swift=models.CharField(max_length=200)
    routing_number=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    country=models.CharField(max_length=200)
    status=models.ForeignKey(Status_type,on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        if not self.supplier_id:  # Only generate ID if it's not already set
            # Get the last language added to calculate the next ID
            last_supplier = Supplier.objects.order_by('supplier_id').last()
            if last_supplier:
                # Extract the number part and increment it
                last_id_number = int(last_supplier.supplier_id[3:])  # Skip 'LAN' prefix
                next_id_number = last_id_number + 1
                # Ensure the ID has 2 digits for padding (e.g., LAN01, LAN02, ...)
                self.supplier_id = f"SUP{next_id_number:02d}"  # 2 digits for padding
            else:
                # If no languages exist, start with 'LAN01'
                self.supplier_id = 'SUP01'

        super(Supplier, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.supplier_id  
   
    
class Contact_details(models.Model):
    supplier=models.ForeignKey(Supplier,on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=50,blank=True,null=True)
    designation=models.CharField(max_length=100,blank=True,null=True)
    mobile=models.PositiveIntegerField(blank=True,null=True)
    whatsapp=models.PositiveIntegerField(blank=True,null=True)
    email=models.EmailField(blank=True,null=True)
    
    def __str__(self):
        return self.supplier.supplier_id
    
    

    
    
    
class Package(models.Model):
    
    transport_Choices=[
        ('Sharing','Sharing'),
        ('Private','Private'),
        ('Without Transfer','Without Transfer'),
        ('Tickets Only','Tickets Only')
    ]
    
    
    package_id=models.CharField(max_length=10,primary_key=True,editable=False)
    package_code=models.CharField(max_length=20)
    package_title=models.CharField(max_length=30)
    package_category=models.ForeignKey(Category,on_delete=models.CASCADE,to_field='category_id')
    package_city=models.CharField(max_length=30)
    web_id=models.CharField(max_length=200)
    web_sku=models.CharField(max_length=200)
    website_link=models.CharField(max_length=300)
    short_description=models.TextField(max_length=300)
    highlights=models.TextField(max_length=300)
    description=models.TextField(max_length=1000)
    inclusions=models.CharField(max_length=500)
    exclusions=models.CharField(max_length=500)
    transportation=models.CharField(choices=transport_Choices,max_length=30)
    language=models.ManyToManyField(Language)
    open_hours=models.CharField(max_length=30)
    sunday=models.BooleanField(default=True,blank=True,null=True)
    monday=models.BooleanField(default=True,blank=True,null=True)
    tuesday=models.BooleanField(default=True,blank=True,null=True)
    wednesday=models.BooleanField(default=True,blank=True,null=True)
    thursday=models.BooleanField(default=True,blank=True,null=True)
    friday=models.BooleanField(default=True,blank=True,null=True)
    saturday=models.BooleanField(default=True,blank=True,null=True)
    location=models.CharField(max_length=100)
    adult_rate=models.CharField(max_length=20)
    child_rate=models.CharField(max_length=20)
    infant_rate=models.CharField(max_length=20)
    adult_age=models.CharField(max_length=10)
    child_age=models.CharField(max_length=10)
    infant_age=models.CharField(max_length=10)
    status=models.ForeignKey(Status_type,on_delete=models.CASCADE)
    image_link=models.CharField(max_length=600)
    video_link=models.CharField(max_length=600)
    is_deleted=models.BooleanField(default=False)

    
    def __str__(self):
        return self.package_title
    
    def save(self, *args, **kwargs):
        if not self.package_id:  # Only generate ID if it's not already set
            # Get the last language added to calculate the next ID
            last_package = Package.objects.order_by('package_id').last()
            if last_package:
                # Extract the number part and increment it
                last_id_number = int(last_package.package_id[3:])  # Skip 'LAN' prefix
                next_id_number = last_id_number + 1
                # Ensure the ID has 2 digits for padding (e.g., LAN01, LAN02, ...)
                self.package_id = f"PAC{next_id_number:02d}"  # 2 digits for padding
            else:
                # If no languages exist, start with 'LAN01'
                self.package_id = 'PAC01'

        super(Package, self).save(*args, **kwargs)
    

class Package_images(models.Model):
    package=models.ForeignKey(Package,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='package_images/',blank=True,null=True)

    def __str__(self):
        return self.package.package_title
    
    
class Hero_image(models.Model):
    package=models.ForeignKey(Package,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='Hero_images/',blank=True,null=True)
    
    def __str__(self):
        return self.package.package_title
    
    
class Video(models.Model):
    package=models.ForeignKey(Package,on_delete=models.CASCADE)
    video=models.FileField(upload_to='videos/',blank=True,null=True)
    
    def __str__(self):
        return self.package.package_title
    
    
    
class Supplier_allocation(models.Model):
    package=models.ForeignKey(Package,on_delete=models.CASCADE)
    supplier=models.ManyToManyField(Supplier)
    
    def __str__(self):
        return self.package.package_id
    
    
    
class Parent(models.Model):
    name = models.CharField(max_length=100)

class Child(models.Model):
    parent = models.ForeignKey(Parent, related_name='children', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    
    
    
    

class Company(models.Model):
    company_id=models.CharField(max_length=10,primary_key=True,editable=False)
    name=models.CharField(max_length=100)
    company_type=models.ForeignKey(Company_type,on_delete=models.CASCADE)
    tl_number=models.PositiveIntegerField()
    vat_number=models.PositiveIntegerField()
    address1=models.CharField(max_length=100)
    city1=models.CharField(max_length=100)
    state1=models.CharField(max_length=100)
    country1=models.CharField(max_length=100)
    pincode1=models.PositiveIntegerField()
    phone1=models.PositiveIntegerField()
    address2=models.CharField(max_length=100,blank=True,null=True)
    city2=models.CharField(max_length=100,blank=True,null=True)
    state2=models.CharField(max_length=100,blank=True,null=True)
    country2=models.CharField(max_length=100,blank=True,null=True)
    pincode2=models.PositiveIntegerField(blank=True,null=True)
    phone2=models.PositiveIntegerField(blank=True,null=True)
    mobile=models.PositiveIntegerField()
    email=models.EmailField()
    trade_license=models.FileField(upload_to='company_trade_license/')
    vat_certificate=models.FileField(upload_to='company_vat_cerificate/')
    account_name=models.CharField(max_length=200)
    bank_name=models.CharField(max_length=200)
    account_number=models.PositiveIntegerField()
    iban=models.CharField(max_length=200)
    swift=models.CharField(max_length=200)
    routing_number=models.PositiveIntegerField()
    branch=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    country=models.CharField(max_length=200)
    status=models.ForeignKey(Status_type,on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        if not self.company_id:  # Only generate ID if it's not already set
            # Get the last language added to calculate the next ID
            last_company = Company.objects.order_by('company_id').last()
            if last_company:
                # Extract the number part and increment it
                last_id_number = int(last_company.company_id[3:])  # Skip 'LAN' prefix
                next_id_number = last_id_number + 1
                # Ensure the ID has 2 digits for padding (e.g., LAN01, LAN02, ...)
                self.company_id = f"COM{next_id_number:02d}"  # 2 digits for padding
            else:
                # If no languages exist, start with 'LAN01'
                self.company_id = 'COM01'

        super(Company, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.name  
    
    
class Company_contact_details(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=50,blank=True,null=True)
    designation=models.CharField(max_length=100,blank=True,null=True)
    mobile=models.PositiveIntegerField(blank=True,null=True)
    whatsapp=models.PositiveIntegerField(blank=True,null=True)
    email=models.EmailField(blank=True,null=True)
    
    def __str__(self):
        return self.company.company_id
    
    
    
    
class Payment_mode(models.Model):
    payment_id=models.CharField(max_length=10,primary_key=True,editable=False)
    payment_mode=models.CharField(max_length=50,unique=True)
    
    def save(self, *args, **kwargs):
        if not self.payment_id:  # Only generate ID if it's not already set
            # Get the last language added to calculate the next ID
            last_payment = Payment_mode.objects.order_by('payment_id').last()
            if last_payment:
                # Extract the number part and increment it
                last_id_number = int(last_payment.payment_id[3:])  # Skip 'LAN' prefix
                next_id_number = last_id_number + 1
                # Ensure the ID has 2 digits for padding (e.g., LAN01, LAN02, ...)
                self.payment_id = f"PAY{next_id_number:02d}"  # 2 digits for padding
            else:
                # If no languages exist, start with 'LAN01'
                self.payment_id = 'PAY01'

        super(Payment_mode, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.payment_mode
    
    
    
class Driver(models.Model):
    type_Choices=[
        ('Limousine','Limousine'),
        ('Transportation','Transportation'),
        ('Tourism','Tourism'),
        ('Stretch limo','Stretch limo')
    ]
    
    driver_id=models.CharField(max_length=10,primary_key=True,editable=False)
    name=models.CharField(max_length=100)
    driver_type=models.CharField(choices=type_Choices,max_length=100)
    vehicle_make=models.CharField(max_length=100)
    vehicle_brand=models.CharField(max_length=100)
    vehicle_year=models.CharField(max_length=10)
    mobile1=models.PositiveIntegerField()
    mobile2=models.PositiveIntegerField()
    whatsapp1=models.PositiveIntegerField()
    whatsapp2=models.PositiveIntegerField()
    email=models.EmailField()
    vehicle_registration=models.CharField(max_length=100)
    rc_expiry=models.DateField()
    dl_number=models.CharField(max_length=100)
    dl_expiry=models.DateField()
    passport_number=models.CharField(max_length=100)
    passport_expiry=models.DateField()
    emirates_id_number=models.CharField(max_length=100)
    emirates_id_expiry=models.DateField()
    visa_number=models.CharField(max_length=100)
    visa_expiry=models.DateField()
    vehicle_rc=models.FileField(upload_to='driver_vehicle_rc/')
    insurance=models.FileField(upload_to='driver_vehicle_insurance/')
    driving_license=models.FileField(upload_to='driving_license/')
    passport=models.FileField(upload_to='driver_passport/')
    emirates_id=models.FileField(upload_to='driver_emirates_id/')
    visa=models.FileField(upload_to='driver_visa/')
    photos=models.FileField(upload_to='driver_photos/')
    status=models.ForeignKey(Status_type,on_delete=models.CASCADE)


    def save(self, *args, **kwargs):
        if not self.driver_id:  # Only generate ID if it's not already set
            # Get the last language added to calculate the next ID
            last_driver = Driver.objects.order_by('driver_id').last()
            if last_driver:
                # Extract the number part and increment it
                last_id_number = int(last_driver.driver_id[3:])  # Skip 'LAN' prefix
                next_id_number = last_id_number + 1
                # Ensure the ID has 2 digits for padding (e.g., LAN01, LAN02, ...)
                self.driver_id = f"DVR{next_id_number:02d}"  # 2 digits for padding
            else:
                # If no languages exist, start with 'LAN01'
                self.driver_id = 'DVR01'

        super(Driver, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.driver_id 




class Guide(models.Model):
    guide_id=models.CharField(max_length=10,primary_key=True,editable=False)
    name=models.CharField(max_length=100)
    abudhabi_license=models.BooleanField(default=True)
    dubai_license=models.BooleanField(default=True)
    rak_license=models.BooleanField(default=True)
    sharjah_license=models.BooleanField(default=True)
    fujairah_license=models.BooleanField(default=True)
    mobile1=models.PositiveIntegerField()
    mobile2=models.PositiveIntegerField()
    whatsapp1=models.PositiveIntegerField()
    whatsapp2=models.PositiveIntegerField()
    email=models.EmailField()
    license_number=models.CharField(max_length=100)
    license_expiry=models.DateField()
    language=models.ManyToManyField(Language)
    passport_number=models.CharField(max_length=100)
    passport_expiry=models.DateField()
    emirates_id_number=models.CharField(max_length=100)
    emirates_id_expiry=models.DateField()
    visa_number=models.CharField(max_length=100)
    visa_expiry=models.DateField()
    license_copy=models.FileField(upload_to='guide_license/')
    passport=models.FileField(upload_to='guide_passport/')
    emirates_id=models.FileField(upload_to='guide_emirates_id/')
    visa=models.FileField(upload_to='guide_visa/')
    photos=models.FileField(upload_to='driver_photos/')
    status=models.ForeignKey(Status_type,on_delete=models.CASCADE)


    def save(self, *args, **kwargs):
        if not self.guide_id:  # Only generate ID if it's not already set
            # Get the last language added to calculate the next ID
            last_guide = Guide.objects.order_by('guide_id').last()
            if last_guide:
                # Extract the number part and increment it
                last_id_number = int(last_guide.guide_id[3:])  # Skip 'LAN' prefix
                next_id_number = last_id_number + 1
                # Ensure the ID has 2 digits for padding (e.g., LAN01, LAN02, ...)
                self.guide_id = f"GUI{next_id_number:02d}"  # 2 digits for padding
            else:
                # If no languages exist, start with 'LAN01'
                self.guide_id = 'GUI01'

        super(Guide, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.guide_id 









class Reminder(models.Model):
    reminder_id=models.CharField(max_length=10,primary_key=True,editable=False)
    name=models.CharField(max_length=50,unique=True)
    description=models.CharField(max_length=200,unique=True)
    date=models.DateField()
    time=models.TimeField()
    
    def save(self, *args, **kwargs):
        if not self.reminder_id:  # Only generate ID if it's not already set
            # Get the last language added to calculate the next ID
            last_reminder = Reminder.objects.order_by('reminder_id').last()
            if last_reminder:
                # Extract the number part and increment it
                last_id_number = int(last_reminder.reminder_id[3:])  # Skip 'LAN' prefix
                next_id_number = last_id_number + 1
                # Ensure the ID has 2 digits for padding (e.g., LAN01, LAN02, ...)
                self.reminder_id = f"REM{next_id_number:02d}"  # 2 digits for padding
            else:
                # If no languages exist, start with 'LAN01'
                self.reminder_id = 'REM01'

        super(Reminder, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.reminder_id 
    
    
    
class Vehicle_type(models.Model):
    type_name=models.CharField(max_length=100)
    description=models.CharField(max_length=200,blank=True,null=True)
    
    def __str__(self):
        return self.type_name



class Booking(models.Model):
    payment_status_choices=[
        ('Paid','Paid'),
        ('Unpaid','Unpaid'),
    ]    
    booked_date = models.DateField(auto_now_add=True)
    booked_by=models.CharField(max_length=100,default="mujeeb")
    booking_id=models.CharField(max_length=10,primary_key=True,editable=False)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    guest_name=models.CharField(max_length=200)
    email=models.EmailField()
    contact_number=models.CharField(max_length=20)
    whatsapp_number=models.CharField(max_length=20)
    payment_ref_no=models.CharField(max_length=50)
    payment_status=models.CharField(choices=payment_status_choices,max_length=20)
    payment_mode=models.ForeignKey(Payment_mode,on_delete=models.CASCADE)
    status=models.ForeignKey(Status_type,on_delete=models.CASCADE)


    
    
    def save(self, *args, **kwargs):
        if not self.booking_id:  # Only generate ID if it's not already set
            # Get the last language added to calculate the next ID
            last_booking = Booking.objects.order_by('booking_id').last()
            if last_booking:
                # Extract the number part and increment it
                last_id_number = int(last_booking.booking_id[3:])  # Skip 'LAN' prefix
                next_id_number = last_id_number + 1
                # Ensure the ID has 2 digits for padding (e.g., LAN01, LAN02, ...)
                self.booking_id = f"BOK{next_id_number:02d}"  # 2 digits for padding
            else:
                # If no languages exist, start with 'LAN01'
                self.booking_id = 'BOK01'

        super(Booking, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.booking_id 
    
    

class Booking_Trip_details(models.Model):
    booking=models.ForeignKey(Booking,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    package=models.ForeignKey(Package,on_delete=models.CASCADE)
    trip_date=models.DateField()
    trip_time=models.TimeField()
    no_of_adult=models.PositiveIntegerField()
    no_of_child=models.PositiveIntegerField()
    no_of_infant=models.PositiveIntegerField()
    rate_of_adult=models.PositiveIntegerField()
    rate_of_child=models.PositiveIntegerField()
    rate_of_infant=models.PositiveIntegerField()
    pickup_location=models.CharField(max_length=100,null=True,blank=True)
    drop_location=models.CharField(max_length=100,null=True,blank=True)
    room_no=models.CharField(max_length=100,null=True,blank=True)
    pickup_time=models.TimeField(null=True,blank=True)
    transfer_type=models.CharField(max_length=100,null=True,blank=True)
    vehicle_type=models.ForeignKey(Vehicle_type,on_delete=models.CASCADE,null=True,blank=True)
    vehicle_name=models.CharField(max_length=100,null=True,blank=True)
    no_of_luggage=models.PositiveIntegerField(null=True,blank=True)
    flight_time=models.TimeField(null=True,blank=True)
    remark=models.CharField(max_length=500,null=True,blank=True)

    
    
    
    def __str__(self):
        return self.booking.booking_id 

