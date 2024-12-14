from django.contrib import admin
from .models import *



class Languageadmin(admin.ModelAdmin):
    list_display=('language_id','language_name')
    

admin.site.register(Language,Languageadmin)
admin.site.register(Category)
admin.site.register(Package_images)
admin.site.register(Package)
admin.site.register(Supplier_type)
admin.site.register(Supplier)
admin.site.register(Status_type)
admin.site.register(Contact_details)
admin.site.register(Supplier_allocation)
admin.site.register(Company)
admin.site.register(Company_type)
admin.site.register(Company_contact_details)
admin.site.register(Payment_mode)