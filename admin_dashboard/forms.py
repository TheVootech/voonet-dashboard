from django import forms
from .models import *
from django.forms import inlineformset_factory


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget",MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

class Package_form(forms.ModelForm):
    class Meta:
        model=Package
        fields='__all__'
        
        
        widgets = {
            'package_code': forms.TextInput(attrs={
                'class': 'form-control border border-secondary pl-2 pr-2',
                'style': 'font-size: 17px;border-radius:5px;'
            }),
            'package_title': forms.TextInput(attrs={
                'class': 'form-control border border-secondary pl-2 pr-2',
                'style': 'font-size: 17px;border-radius:5px;'
            }),
            'package_category': forms.Select(attrs={
                'class': 'form-select bg-none border border-secondary',
                'style': 'background-color: transparent; border-radius: 5px;'
            }),
            'package_city': forms.TextInput(attrs={
                'class': 'form-control border border-secondary pl-2 pr-2',
                'style': 'font-size: 17px;border-radius:5px;'
            }),
            'web_id': forms.TextInput(attrs={
                'class': 'form-control border border-secondary pl-2 pr-2',
                'style': 'font-size: 17px;border-radius:5px;'
            }),
            'web_sku': forms.TextInput(attrs={
                'class': 'form-control border border-secondary pl-2 pr-2',
                'style': 'font-size: 17px;border-radius:5px;'
            }),
            'website_link': forms.TextInput(attrs={
                'class': 'form-control border border-secondary pl-2 pr-2',
                'style': 'font-size: 17px;border-radius:5px;' 
            }),
            'short_description': forms.Textarea(attrs={
                'class': 'form-control border border-secondary pl-2 pr-2',
                'style': 'font-size: 17px;border-radius:5px;height:100px !important;' 
            }),
            'highlights': forms.Textarea(attrs={
                'class': 'form-control border border-secondary pl-2 pr-2',
                'style': 'font-size: 17px;border-radius:5px;height:100px !important;' 
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control border border-secondary pl-2 pr-2',
                'style': 'font-size: 17px;border-radius:5px;height:100px !important;' 
            }),
            'inclusions': forms.Textarea(attrs={
                'class': 'form-control border border-secondary pl-2 pr-2',
                'style': 'font-size: 17px;border-radius:5px;height:100px !important;' 
            }),
            'exclusions': forms.Textarea(attrs={
                'class': 'form-control border border-secondary pl-2 pr-2',
                'style': 'font-size: 17px;border-radius:5px;height:100px !important;' 
            }),
            'transportation': forms.Select(attrs={
                'class': 'form-select bg-none border border-secondary',
                'style': 'background-color: transparent; border-radius: 5px;'
            }),
             'language': forms.SelectMultiple(attrs={
                'class': 'form-select bg-none border border-secondary',
                'style': 'background-color: transparent; border-radius: 5px;height:50px !important;'
            }),
            'sunday': forms.CheckboxInput(attrs={
            }),
            'monday': forms.CheckboxInput(attrs={
            }),
            'tuesday': forms.CheckboxInput(attrs={
            }),
            'wednesday': forms.CheckboxInput(attrs={
            }),
            'thursday': forms.CheckboxInput(attrs={
            }),
            'friday': forms.CheckboxInput(attrs={
            }),
            'saturday': forms.CheckboxInput(attrs={
            }),
            'open_hours': forms.TextInput(attrs={
                'class': 'form-control border border-secondary pl-2 pr-2',
                'style': 'font-size: 17px;border-radius:5px;' 
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control border border-secondary pl-2 pr-2',
                'style': 'font-size: 17px;border-radius:5px;' 
            }),
            'adult_rate': forms.TextInput(attrs={
                'class': 'form-control border border-secondary pl-2 pr-2',
                'style': 'font-size: 17px;border-radius:5px;',
            }),
            'child_rate': forms.TextInput(attrs={
                'class': 'form-control border border-secondary pl-2 pr-2',
                'style': 'font-size: 17px;border-radius:5px;' 
            }),
            'infant_rate': forms.TextInput(attrs={
                'class': 'form-control border border-secondary pl-2 pr-2',
                'style': 'font-size: 17px;border-radius:5px;' 
            }),
            'adult_age': forms.TextInput(attrs={
                'class': 'form-control border border-secondary pl-2 pr-2',
                'style': 'font-size: 17px;border-radius:5px;' 
            }),
            'child_age': forms.TextInput(attrs={
                'class': 'form-control border border-secondary pl-2 pr-2',
                'style': 'font-size: 17px;border-radius:5px;' 
            }),
            'infant_age': forms.TextInput(attrs={
                'class': 'form-control border border-secondary pl-2 pr-2',
                'style': 'font-size: 17px;border-radius:5px;' 
            }),
            'status': forms.Select(attrs={
                'class': 'form-select bg-none border border-secondary',
                'style': 'background-color: transparent; border-radius: 5px;'
            }),
            'image_link': forms.TextInput(attrs={
                'class': 'form-control border border-secondary pl-2 pr-2',
                'style': 'font-size: 17px;border-radius:5px;' 
            }),
            'video_link': forms.TextInput(attrs={
                'class': 'form-control border border-secondary pl-2 pr-2',
                'style': 'font-size: 17px;border-radius:5px;' 
            }),
            
        }
        
        
class Package_image_form(forms.ModelForm):
    image=MultipleFileField(label='',required=False)
    class Meta:
        model=Package_images
        fields=['image']
        

class Hero_image_form(forms.ModelForm):
    image=MultipleFileField(label='',required=False)
    class Meta:
        model=Hero_image
        fields=['image']
        
        
        
class Video_form(forms.ModelForm):
    video=MultipleFileField(label='',required=False)
    class Meta:
        model=Video
        fields=['video']
        
        
class Category_form(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'
        
        widgets = {
                'category_name': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
        }
    
    

        
class Languages_form(forms.ModelForm):
    class Meta:
        model=Language
        fields='__all__' 
        
        widgets = {
                'language_name': forms.TextInput(attrs={
                    'class': 'form-control  border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
        }
 
 
 
class Contact_details_form(forms.ModelForm):
    class Meta:
        model=Contact_details
        exclude=['supplier']
        
        widgets={
                'name': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'designation': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'mobile': forms.NumberInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'whatsapp': forms.NumberInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'email': forms.EmailInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
        }
        
Contact_details_formset=inlineformset_factory(
    Supplier,Contact_details,form=Contact_details_form,extra=1,can_delete=True
)
        
       
        
class Supplier_form(forms.ModelForm):
    class Meta:
        model=Supplier
        exclude=['supplier_id']
        
        widgets={
                'name': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'category':  forms.Select(attrs={
                    'class': 'form-select bg-none border border-secondary',
                    'style': 'background-color: transparent; border-radius: 5px;'
                }),
                'supplier_type':  forms.Select(attrs={
                    'class': 'form-select bg-none border border-secondary',
                    'style': 'background-color: transparent; border-radius: 5px;'
                }),
                'tl_number': forms.NumberInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'vat_number': forms.NumberInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'address1': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'city1': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'state1': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'country1': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'pincode1': forms.NumberInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'phone1': forms.NumberInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'address2': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'city2': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'state2': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'country2': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'pincode2': forms.NumberInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'phone2': forms.NumberInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'mobile': forms.NumberInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'email': forms.EmailInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'trade_license': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'vat_certificate': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'account_name': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'bank_name': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'account_number': forms.NumberInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'iban': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'swift': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'routing_number': forms.NumberInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'branch': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'city': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'country': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'status':  forms.Select(attrs={
                    'class': 'form-select bg-none border border-secondary',
                    'style': 'background-color: transparent; border-radius: 5px;'
                }),
                
        }



class Allocate_supplier_form(forms.ModelForm):
    class Meta:
        model = Supplier_allocation
        fields = ['package', 'supplier']
        widgets = {
            'package': forms.Select(attrs={'class': 'form-select bg-none', 'style': 'background-color: transparent; border-radius: 5px;'}),
            'supplier': forms.SelectMultiple(attrs={'class': 'form-select bg-none', 'style': 'background-color: transparent; border-radius: 5px;'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['package'].queryset = Package.objects.filter(supplier_allocation__isnull=True).distinct()

        
        
        
        
        
class Edit_allocate_supplier_form(forms.ModelForm):
    class Meta:
        model=Supplier_allocation
        fields=['package','supplier']
        
        widgets={
            'package':forms.TextInput(attrs={
                 'class': 'form-select bg-none border border-secondary',
                 'style': 'background-color: transparent; border-radius: 5px;',
                 'readonly': 'readonly',
            }),
            'supplier':forms.SelectMultiple(attrs={
                 'class': 'form-select bg-none border border-secondary',
                 'style': 'background-color: transparent; border-radius: 5px;'
            })
        }
                
        
        
class Edit_Contact_details_form(forms.ModelForm):
    class Meta:
        model=Contact_details
        exclude=['supplier']
        
        widgets={
                'name': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'designation': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'mobile': forms.NumberInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'whatsapp': forms.NumberInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'email': forms.EmailInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
        }
        
Edit_Contact_details_formset=inlineformset_factory(
    Supplier,Contact_details,form=Edit_Contact_details_form,extra=0,can_delete=True
)
        
       
        
class Edit_Supplier_form(forms.ModelForm):
    class Meta:
        model=Supplier
        exclude=['supplier_id']
        
        widgets={
                'name': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'category':  forms.Select(attrs={
                    'class': 'form-select bg-none border border-secondary',
                    'style': 'background-color: transparent; border-radius: 5px;'
                }),
                'supplier_type':  forms.Select(attrs={
                    'class': 'form-select bg-none border border-secondary',
                    'style': 'background-color: transparent; border-radius: 5px;'
                }),
                'tl_number': forms.NumberInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'vat_number': forms.NumberInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'address1': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'city1': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'state1': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'country1': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'pincode1': forms.NumberInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'phone1': forms.NumberInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'address2': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'city2': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'state2': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'country2': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'pincode2': forms.NumberInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'phone2': forms.NumberInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'mobile': forms.NumberInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'email': forms.EmailInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'trade_license': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'vat_certificate': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'account_name': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'bank_name': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'account_number': forms.NumberInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'iban': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'swift': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'routing_number': forms.NumberInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'branch': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'city': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'country': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'status':  forms.Select(attrs={
                    'class': 'form-select bg-none border border-secondary',
                    'style': 'background-color: transparent; border-radius: 5px;'
                }),
                
        }
        
        
class Company_form(forms.ModelForm):
    class Meta:
        model=Company
        exclude=['company_id']
        
        
        
        widgets={
                'name': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'company_type':  forms.Select(attrs={
                    'class': 'form-select bg-none border border-secondary',
                    'style': 'background-color: transparent; border-radius: 5px;'
                }),
                'tl_number': forms.NumberInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'vat_number': forms.NumberInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'address1': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'city1': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'state1': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'country1': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'pincode1': forms.NumberInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'phone1': forms.NumberInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'address2': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'city2': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'state2': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'country2': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'pincode2': forms.NumberInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'phone2': forms.NumberInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'mobile': forms.NumberInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'email': forms.EmailInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'trade_license': forms.FileInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'vat_certificate': forms.FileInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'account_name': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'bank_name': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'account_number': forms.NumberInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'iban': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'swift': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'routing_number': forms.NumberInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'branch': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'city': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'country': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'status':  forms.Select(attrs={
                    'class': 'form-select bg-none border border-secondary',
                    'style': 'background-color: transparent; border-radius: 5px;'
                }),
                
        }




class Company_contact_details_form(forms.ModelForm):
    class Meta:
        model=Company_contact_details
        exclude=['company']
        
        widgets={
                'name': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'designation': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'mobile': forms.NumberInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'whatsapp': forms.NumberInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'email': forms.EmailInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
        }
        
Company_contact_details_formset=inlineformset_factory(
    Company,Company_contact_details,form=Company_contact_details_form,extra=1,can_delete=True
)



class Payment_form(forms.ModelForm):
    class Meta:
        model=Payment_mode
        exclude=['payment_id']
        
        widgets={
                'payment_mode': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
         }
        
        
class Driver_form(forms.ModelForm):
    class Meta:
        model=Driver
        exclude=['driver_id']
        
        widgets={
                'name': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'driver_type': forms.Select(attrs={
                    'class': 'form-select bg-none border border-secondary',
                    'style': 'background-color: transparent; border-radius: 5px;'
                }),
                'vehicle_make': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'vehicle_brand': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'vehicle_year': forms.NumberInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;',
                }),
                'mobile1': forms.NumberInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;',
                }),
                'mobile2': forms.NumberInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;',
                }),
                'whatsapp1': forms.NumberInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;',
                }),
                'whatsapp2': forms.NumberInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;',
                }),
                'email': forms.EmailInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;',
                }),
                'vehicle_registration': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'rc_expiry': forms.DateInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;',
                    'type':'date'
                }),
                'dl_number': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'dl_expiry': forms.DateInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;',
                    'type':'date'
                }),
                'passport_number': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'passport_expiry': forms.DateInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;',
                    'type':'date'
                }),
                'emirates_id_number': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'emirates_id_expiry': forms.DateInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;',
                    'type':'date'
                }),
                'visa_number': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'visa_expiry': forms.DateInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;',
                    'type':'date'
                }),
                'vehicle_rc': forms.FileInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'insurance': forms.FileInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'driving_license': forms.FileInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'passport': forms.FileInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'emirates_id': forms.FileInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'visa': forms.FileInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'photos': forms.FileInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'status':  forms.Select(attrs={
                    'class': 'form-select bg-none border border-secondary',
                    'style': 'background-color: transparent; border-radius: 5px;'
                }),
                 
                
         }
        
        
        
        
        
class Guide_form(forms.ModelForm):
    class Meta:
        model=Guide
        exclude=['guide_id']
        
        widgets={
                'name': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                
                'abudhabi_license': forms.CheckboxInput(attrs={
                }),
                'dubai_license': forms.CheckboxInput(attrs={
                }),
                'rak_license': forms.CheckboxInput(attrs={
                }),
                'sharjah_license': forms.CheckboxInput(attrs={
                }),
                'fujairah_license': forms.CheckboxInput(attrs={
                }),
                
                'mobile1': forms.NumberInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;',
                }),
                'mobile2': forms.NumberInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;',
                }),
                'whatsapp1': forms.NumberInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;',
                }),
                'whatsapp2': forms.NumberInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;',
                }),
                'email': forms.EmailInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;',
                }),
                'license_number': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'license_expiry': forms.DateInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;',
                    'type':'date'
                }),
                'language': forms.SelectMultiple(attrs={
                    'class': 'form-select bg-none border border-secondary',
                    'style': 'background-color: transparent; border-radius: 5px;height:50px !important;'
                }),
                'passport_number': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'passport_expiry': forms.DateInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;',
                    'type':'date'
                }),
                'emirates_id_number': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'emirates_id_expiry': forms.DateInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;',
                    'type':'date'
                }),
                'visa_number': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'visa_expiry': forms.DateInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;',
                    'type':'date'
                }),
                'license_copy': forms.FileInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),            
                'passport': forms.FileInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'emirates_id': forms.FileInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'visa': forms.FileInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'photos': forms.FileInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'status':  forms.Select(attrs={
                    'class': 'form-select bg-none border border-secondary',
                    'style': 'background-color: transparent; border-radius: 5px;'
                }),

         }
        
        
        
        
class Reminder_form(forms.ModelForm):
    class Meta:
        model=Reminder
        exclude=['reminder_id']
        
        widgets={
                'name': forms.TextInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;'
                }),
                'description': forms.Textarea(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;height:80px !important;'
                }),
                'date': forms.DateInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;',
                    'type':'date',
                }),
                'time': forms.TimeInput(attrs={
                    'class': 'form-control border border-secondary pl-2 pr-2',
                    'style': 'font-size: 17px;border-radius:5px;',
                    'type':'time',
                }),
         }