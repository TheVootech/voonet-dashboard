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


class Bookings(models.Model):
    company=models.CharField(max_length=120)
    contact_person=models.CharField(max_length=120)
    package=models.CharField(max_length=120)
    adult=models.PositiveIntegerField()
    child=models.PositiveIntegerField()
    infant=models.PositiveIntegerField()
    foc=models.PositiveIntegerField()
    tour_date=models.DateField()
    tour_time=models.TimeField()
    pickup_location=models.CharField(max_length=200)
    guest_name=models.CharField(max_length=200)
    email=models.EmailField()
    contact_number=models.CharField(max_length=20)
    payment_ref_no=models.CharField(max_length=50)
    room_no=models.CharField(max_length=20)
    payment_status=models.CharField(max_length=20)
    special_requirements=models.CharField(max_length=200)
    
    def __str__(self):
        return self.guest_name
    
    
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
    trade_license=models.CharField(max_length=200)
    vat_certificate=models.CharField(max_length=200)
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
        return self.company_id  
    
    
class Company_contact_details(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=50,blank=True,null=True)
    designation=models.CharField(max_length=100,blank=True,null=True)
    mobile=models.PositiveIntegerField(blank=True,null=True)
    whatsapp=models.PositiveIntegerField(blank=True,null=True)
    email=models.EmailField(blank=True,null=True)
    
    def __str__(self):
        return self.company.company_id