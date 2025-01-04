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
                'class': 'form-control',
                'placeholder':'Enter Package Code ',
            }),
            'package_title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Enter Package Title ',
            }),
            'package_category': forms.Select(attrs={
                'class': 'form-select',
                'style': 'background-color: transparent; border: none; border-bottom: 2px solid #D3D3D3; border-radius: 0;',
            }),
            'package_city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Enter Package  City ',
            }),
            'web_id': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Enter WEB ID ',
            }),
            'web_sku': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Enter WEB SKU ',
            }),
            'website_link': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Enter Website Link ', 
            }),
            'short_description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder':'Enter Short Description ',
                'style': 'height:100px !important;' 
            }),
            'highlights': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder':'Enter Highlights ',
                'style': 'height:100px !important;' 
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder':'Enter Description ',
                'style': 'height:80px !important;' 
            }),
            'inclusions': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder':'Enter Inclusions ',
                'style': 'height:80px !important;' 
            }),
            'exclusions': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder':'Enter Exclusions ',
                'style': 'height:80px !important;' 
            }),
            'transportation': forms.Select(attrs={
                'class': 'form-select',
                'style': 'background-color: transparent; border: none; border-bottom: 2px solid #D3D3D3; border-radius: 0;',

            }),
             'language': forms.SelectMultiple(attrs={
                'class': 'form-select'
            }),
            'sunday': forms.CheckboxInput(attrs={
                'class':'form-check-input',
            }),
            'monday': forms.CheckboxInput(attrs={
                'class':'form-check-input',
            }),
            'tuesday': forms.CheckboxInput(attrs={
                'class':'form-check-input',
            }),
            'wednesday': forms.CheckboxInput(attrs={
                'class':'form-check-input',
            }),
            'thursday': forms.CheckboxInput(attrs={
                'class':'form-check-input',
            }),
            'friday': forms.CheckboxInput(attrs={
                'class':'form-check-input',
            }),
            'saturday': forms.CheckboxInput(attrs={
                'class':'form-check-input',
            }),
            'open_hours': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Enter Open Hours ',
                 
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Enter Location ',
            }),
            'adult_rate': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Enter Adult Price ',


            }),
            'child_rate': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Enter Child Price ',
            }),
            'infant_rate': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Enter Infant Price ',
            }),
            'adult_age': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Enter Adult Age ',
            }),
            'child_age': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Enter Child Price ',
            }),
            'infant_age': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Enter Infant Price ',
            }),
            'status': forms.Select(attrs={
                'class': 'form-select',
                'style': 'background-color: transparent; border: none; border-bottom: 2px solid #D3D3D3; border-radius: 0;',
            }),
            'image_link': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Enter Image Link ',
            }),
            'video_link': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Enter Video Link ',
            }),
            
        }
        
        
class Package_image_form(forms.ModelForm):
    image=MultipleFileField(label='',required=False)
    class Meta:
        model=Package_images
        fields=['image']
        
        widgets = {
                'image': forms.FileInput(attrs={
                    'class': 'form-control',
                }),
                }
        

class Hero_image_form(forms.ModelForm):
    image=MultipleFileField(label='',required=False)
    class Meta:
        model=Hero_image
        fields=['image']
        
        widgets = {
            'image': forms.FileInput(attrs={
                'class': 'form-control',
            }),
            }
        
        
        
class Video_form(forms.ModelForm):
    video=MultipleFileField(label='',required=False)
    class Meta:
        model=Video
        fields=['video']
        
        widgets = {
            'video': forms.FileInput(attrs={
                'class': 'form-control',
            }),
        }
        
        
class Category_form(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'
        
        widgets = {
                'category_name': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder':'Enter Category Name'
                }),
                'no_of_adult': forms.CheckboxInput(attrs={
                    'class':'form-check-input',
                }),
                'no_of_child': forms.CheckboxInput(attrs={
                    'class':'form-check-input',
                }),
                'no_of_infant': forms.CheckboxInput(attrs={
                    'class':'form-check-input',
                }),
                'rate_of_adult': forms.CheckboxInput(attrs={
                    'class':'form-check-input',
                }),
                'rate_of_child': forms.CheckboxInput(attrs={
                    'class':'form-check-input',
                }),
                'rate_of_infant': forms.CheckboxInput(attrs={
                    'class':'form-check-input',
                }),
                'pickup_location': forms.CheckboxInput(attrs={
                    'class':'form-check-input',
                }),
                'drop_location': forms.CheckboxInput(attrs={
                    'class':'form-check-input',
                }),
                'room_no': forms.CheckboxInput(attrs={
                    'class':'form-check-input',
                }),
                'remark': forms.CheckboxInput(attrs={
                    'class':'form-check-input',
                }),
                'date': forms.CheckboxInput(attrs={
                    'class':'form-check-input',
                }),
                'time': forms.CheckboxInput(attrs={
                    'class':'form-check-input',
                }),
                'pickup_time': forms.CheckboxInput(attrs={
                    'class':'form-check-input',
                }),
                'transfer_type': forms.CheckboxInput(attrs={
                    'class':'form-check-input',
                }),
                'vehicle_type': forms.CheckboxInput(attrs={
                    'class':'form-check-input',
                }),
                'vehicle_name': forms.CheckboxInput(attrs={
                    'class':'form-check-input',
                }),
                'no_of_luggage': forms.CheckboxInput(attrs={
                    'class':'form-check-input',
                }),
                'flight_time': forms.CheckboxInput(attrs={
                    'class':'form-check-input',
                }),
        }
    
    

        
class Languages_form(forms.ModelForm):
    class Meta:
        model=Language
        fields='__all__' 
        
        widgets = {
                'language_name': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder':'Enter Language Name'
                }),
        }
 
 
 
class Contact_details_form(forms.ModelForm):
    class Meta:
        model=Contact_details
        exclude=['supplier']
        
        widgets={
                'name': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Name'
                }),
                'designation': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Designation'
                }),
                'mobile': forms.NumberInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Mobile'
                }),
                'whatsapp': forms.NumberInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Whatsapp'
                }),
                'email': forms.EmailInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Email'
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
                    'class': 'form-control',
                    'placeholder': 'Enter Supplier Full Name',
                    'required':'required',
                    
                }),
                'category': forms.Select(attrs={
                    'class': 'form-select',
                    'style': 'background-color: transparent; border: none; border-bottom: 2px solid #D3D3D3; border-radius: 0;',
                    
                }),

                'supplier_type':  forms.Select(attrs={
                    'class': 'form-select',
                    'style': 'background-color: transparent; border: none; border-bottom: 2px solid #D3D3D3; border-radius: 0;'
                }),
                'tl_number': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Trade License No :'
                }),
                'vat_number': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter VAT No :'
                }),
                'address1': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Address'
                }),
                'city1': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter City'
                }),
                'state1': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter State'
                }),
                'country1': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Country'
                }),
                'pincode1': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Pincode/Zipcode'
                }),
                'phone1': forms.NumberInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Phone'
                }),
                'address2': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Address'
                }),
                'city2': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter City'
                }),
                'state2': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter State'
                }),
                'country2': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Country'
                }),
                'pincode2': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Pincode/Zipcode'
                }),
                'phone2': forms.NumberInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Phone'
                }),
                'mobile': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Mobile'
                }),
                'email': forms.EmailInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Email ID'
                }),
                'trade_license': forms.FileInput(attrs={
                    'class': 'form-control',

                }),
                'vat_certificate': forms.FileInput(attrs={
                    'class': 'form-control',
                }),
                'account_name': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Account Name'
                }),
                'bank_name': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Bank Name'
                }),
                'account_number': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Account No :'
                }),
                'iban': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter IBAN ID'
                }),
                'swift': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Swift ID'
                }),
                'routing_number': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Routing No :'
                }),
                'branch': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Branch'
                }),
                'city': forms.TextInput(attrs={
                   'class': 'form-control',
                    'placeholder': 'Enter City'
                }),
                'country': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'EnterCountry'
                }),
                'status':  forms.Select(attrs={
                    'class': 'form-select',
                    'style': 'background-color: transparent; border: none; border-bottom: 2px solid #D3D3D3; border-radius: 0;'

                }),
                
        }
        
    
        
   
    

       



class Allocate_supplier_form(forms.ModelForm):
    class Meta:
        model = Supplier_allocation
        fields = ['package', 'supplier']
        widgets = {
            'package': forms.Select(attrs={                    
                    'class': 'form-select',
                    'style': 'background-color: transparent; border: none; border-bottom: 2px solid #D3D3D3; border-radius: 0;',
                }),
            'supplier': forms.SelectMultiple(attrs={'class': 'form-select'}),
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
                    'class': 'form-control',
                    'placeholder': 'Enter Customer Name'
                }),
                'company_type':  forms.Select(attrs={
                    'class': 'form-select',
                    'style': 'background-color: transparent; border: none; border-bottom: 2px solid #D3D3D3; border-radius: 0;',
                }),
                'tl_number': forms.NumberInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Trade License No :'
                }),
                'vat_number': forms.NumberInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter VAT No :'
                }),
                'address1': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Address'
                }),
                'city1': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter City Name'
                }),
                'state1': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter State Name'
                }),
                'country1': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Coutry'
                }),
                'pincode1': forms.NumberInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Pincode/Zipcode'
                }),
                'phone1': forms.NumberInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Phone No :'
                }),
                'address2': forms.TextInput(attrs={
                   'class': 'form-control',
                    'placeholder': 'Enter Address'
                }),
                'city2': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter City Name'
                }),
                'state2': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter State Name'
                }),
                'country2': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Coutry'
                }),
                'pincode2': forms.NumberInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Pincode/Zipcode'
                }),
                'phone2': forms.NumberInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Phone No :'
                }),
                'mobile': forms.NumberInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Mobile No :'
                }),
                'email': forms.EmailInput(attrs={
                     'class': 'form-control',
                    'placeholder': 'Enter Email ID'
                }),
                'trade_license': forms.FileInput(attrs={
                     'class': 'form-control',
                }),
                'vat_certificate': forms.FileInput(attrs={
                     'class': 'form-control',
                }),
                'account_name': forms.TextInput(attrs={
                     'class': 'form-control',
                    'placeholder': 'Enter Account Name'
                }),
                'bank_name': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Bank Name '
                }),
                'account_number': forms.NumberInput(attrs={
                     'class': 'form-control',
                    'placeholder': 'Enter Account No :'
                }),
                'iban': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter IBAN ID'
                }),
                'swift': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Swift ID'
                }),
                'routing_number': forms.NumberInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Routing No :'
                }),
                'branch': forms.TextInput(attrs={
                     'class': 'form-control',
                    'placeholder': 'Enter Branch'
                }),
                'city': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter City Name'
                }),
                'country': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Country'
                }),
                'status':  forms.Select(attrs={
                    'class': 'form-select',
                    'style': 'background-color: transparent; border: none; border-bottom: 2px solid #D3D3D3; border-radius: 0;',
                }),
                
        }




class Company_contact_details_form(forms.ModelForm):
    class Meta:
        model=Company_contact_details
        exclude=['company']
        
        widgets={
                'name': forms.TextInput(attrs={
                     'class': 'form-control',
                    'placeholder': 'Enter Full Name',
                    'required':'required'
                }),
                'designation': forms.TextInput(attrs={
                     'class': 'form-control',
                    'placeholder': 'Enter Designation',
                     'required':'required'

                }),
                'mobile': forms.NumberInput(attrs={
                     'class': 'form-control',
                    'placeholder': 'Enter Mobile No :',
                    'required':'required'
                }),
                'whatsapp': forms.NumberInput(attrs={
                     'class': 'form-control',
                    'placeholder': 'Enter Whatsapp No :',
                    'required':'required'
                }),
                'email': forms.EmailInput(attrs={
                     'class': 'form-control',
                    'placeholder': 'Enter Email ID',
                    'required':'required'
                }),
        }
        
Company_contact_details_formset=inlineformset_factory(
    Company,Company_contact_details,form=Company_contact_details_form,extra=1,can_delete=True
)

Edit_company_contact_details_formset=inlineformset_factory(
    Company,Company_contact_details,form=Company_contact_details_form,extra=0,can_delete=True
)



class Payment_form(forms.ModelForm):
    class Meta:
        model=Payment_mode
        exclude=['payment_id']
        
        widgets={
                'payment_mode': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Payment Mode',
                }),
         }
        
        
class Status_form(forms.ModelForm):
    class Meta:
        model=Status_type
        exclude=['id']
        
        widgets={
                'status': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Status',
                }),
         }
        
class Company_type_form(forms.ModelForm):
    class Meta:
        model=Company_type
        exclude=['id']
        
        widgets={
                'type_name': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Customer Type',
                }),
         }
        
        

class Supplier_type_form(forms.ModelForm):
    class Meta:
        model=Supplier_type
        exclude=['id']
        
        widgets={
                'type_name': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Customer Type',
                }),
         }
        
        
class Driver_form(forms.ModelForm):
    class Meta:
        model=Driver
        exclude=['driver_id']
        
        
        
        widgets={
                'name': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder':'Enter Driver Full Name'
                }),
                'driver_type': forms.Select(attrs={
                    'class': 'form-select',
                    'style': 'background-color: transparent; border: none; border-bottom: 2px solid #D3D3D3; border-radius: 0;',

                }),
                'vehicle_make': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder':'Enter Vehicle Make'
                }),
                'vehicle_brand': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder':'Enter Vehicle Brand'
                }),
                'vehicle_year': forms.NumberInput(attrs={
                    'class': 'form-control',
                    'placeholder':' Enter Vehicle Year',
                    
                }),
                'mobile1': forms.NumberInput(attrs={
                    'class': 'form-control',
                    'placeholder':'Enter Mobile No :',
                }),
                'mobile2': forms.NumberInput(attrs={
                    'class': 'form-control',
                    'placeholder':'Enter Mobile No :',
                }),
                'whatsapp1': forms.NumberInput(attrs={
                    'class': 'form-control',
                    'placeholder':'Enter Whatsapp No :',
                }),
                'whatsapp2': forms.NumberInput(attrs={
                    'class': 'form-control',
                    'placeholder':'Enter Whatsapp No :',
                }),
                'email': forms.EmailInput(attrs={
                    'class': 'form-control',
                    'placeholder':'Enter Email ID',
                }),
                'vehicle_registration': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder':'Enter Vehicle Registration No :',
                }),
                'rc_expiry': forms.DateInput(attrs={
                    'class': 'form-control',
                    'type':'date'
                }),
                'dl_number': forms.TextInput(attrs={
                     'class': 'form-control',
                    'placeholder':'Enter Driving License No :',
                }),
                'dl_expiry': forms.DateInput(attrs={
                     'class': 'form-control',
                    'type':'date'
                }),
                'passport_number': forms.TextInput(attrs={
                     'class': 'form-control',
                    'placeholder':'Enter Passport No :',
                }),
                'passport_expiry': forms.DateInput(attrs={
                     'class': 'form-control',
                    'type':'date'
                }),
                'emirates_id_number': forms.TextInput(attrs={
                     'class': 'form-control',
                    'placeholder':'Enter Emirates ID No :',
                }),
                'emirates_id_expiry': forms.DateInput(attrs={
                    'class': 'form-control',
                    'type':'date'
                }),
                'visa_number': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder':'Enter Visa No :',
                }),
                'visa_expiry': forms.DateInput(attrs={
                    'class': 'form-control',
                    'type':'date'
                }),
                'vehicle_rc': forms.FileInput(attrs={
                    'class': 'form-control',
                }),
                'insurance': forms.FileInput(attrs={
                    'class': 'form-control',
                }),
                'driving_license': forms.FileInput(attrs={
                    'class': 'form-control',
                }),
                'passport': forms.FileInput(attrs={
                    'class': 'form-control',
                }),
                'emirates_id': forms.FileInput(attrs={
                    'class': 'form-control',
                }),
                'visa': forms.FileInput(attrs={
                    'class': 'form-control',
                }),
                'photos': forms.FileInput(attrs={
                    'class': 'form-control',
                }),
                'status':  forms.Select(attrs={
                    'class': 'form-select',
                    'style': 'background-color: transparent; border: none; border-bottom: 2px solid #D3D3D3; border-radius: 0;',
                }),
                 
                
         }
        
        
        
        
        
class Guide_form(forms.ModelForm):
    class Meta:
        model=Guide
        exclude=['guide_id']
        
        widgets={
                'name': forms.TextInput(attrs={
                   'class': 'form-control',
                    'placeholder':'Enter Guide Full Name',
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
                    'class': 'form-control',
                    'placeholder':'Enter Mobile No :',
                }),
                'mobile2': forms.NumberInput(attrs={
                    'class': 'form-control',
                    'placeholder':'Enter Mobile No :',
                }),
                'whatsapp1': forms.NumberInput(attrs={
                    'class': 'form-control',
                    'placeholder':'Enter Whatsapp No :',
                }),
                'whatsapp2': forms.NumberInput(attrs={
                    'class': 'form-control',
                    'placeholder':'Enter Whatsapp No :',
                }),
                'email': forms.EmailInput(attrs={
                    'class': 'form-control',
                    'placeholder':'Enter Email ID ',
                }),
                'license_number': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder':'Enter License No :',
                }),
                'license_expiry': forms.DateInput(attrs={
                    'class': 'form-control',
                    'type':'date'
                }),
                'language': forms.SelectMultiple(attrs={
                    'class': 'form-control select2',
                }),
                'passport_number': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder':'Enter Passport No :',
                }),
                'passport_expiry': forms.DateInput(attrs={
                    'class': 'form-control',
                    'type':'date'
                }),
                'emirates_id_number': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder':'Enter Emirates ID No :',
                }),
                'emirates_id_expiry': forms.DateInput(attrs={
                    'class': 'form-control',
                    'type':'date'
                }),
                'visa_number': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder':'Enter Visa No :',
                }),
                'visa_expiry': forms.DateInput(attrs={
                    'class': 'form-control',
                    'type':'date'
                }),
                'license_copy': forms.FileInput(attrs={
                    'class': 'form-control'
                }),            
                'passport': forms.FileInput(attrs={
                    'class': 'form-control'
                }),
                'emirates_id': forms.FileInput(attrs={
                    'class': 'form-control'
                }),
                'visa': forms.FileInput(attrs={
                    'class': 'form-control'
                }),
                'photos': forms.FileInput(attrs={
                    'class': 'form-control'
                }),
                'status':  forms.Select(attrs={
                    'class': 'form-select',
                    'style': 'background-color: transparent; border: none; border-bottom: 2px solid #D3D3D3; border-radius: 0;',
                }),

         }
        
        
        
        
class Reminder_form(forms.ModelForm):
    class Meta:
        model=Reminder
        exclude=['reminder_id']
        
        widgets={
                'name': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder':'Enter Reminder Name'
                }),
                'description': forms.Textarea(attrs={
                    'class': 'form-control',
                    'placeholder':'Enter Reminder Description',
                    'style':'height:100px !important;'

                }),
                'date': forms.DateInput(attrs={
                    'class': 'form-control',
                    'type':'date',
                }),
                'time': forms.TimeInput(attrs={
                    'class': 'form-control',
                    'type':'time',
                }),
         }
        
        
class Booking_form(forms.ModelForm):
    class Meta:
        model=Booking
        exclude=['booking_id','booked_date','booked_by']
       
        widgets={    
                'company':  forms.Select(attrs={
                    'class': 'form-select',
                    'style': 'background-color: transparent; border: none; border-bottom: 2px solid #D3D3D3; border-radius: 0;',

                }), 
                'contact_person':  forms.Select(attrs={
                    'class': 'form-select',
                    'style': 'background-color: transparent; border: none; border-bottom: 2px solid #D3D3D3; border-radius: 0;',

                }),                
                
                'payment_ref_no': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder':'Enter Payment Reference No :',
                }),
               
                'payment_status': forms.Select(attrs={
                    'class': 'form-select',
                    'style': 'background-color: transparent; border: none; border-bottom: 2px solid #D3D3D3; border-radius: 0;',

                }),
                'payment_mode': forms.Select(attrs={
                    'class': 'form-select',
                    'style': 'background-color: transparent; border: none; border-bottom: 2px solid #D3D3D3; border-radius: 0;',

                }),
                
                'status': forms.Select(attrs={
                    'class': 'form-select',
                    'style': 'background-color: transparent; border: none; border-bottom: 2px solid #D3D3D3; border-radius: 0;',

                }),
                
        
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Initialize the package queryset as empty by default
        self.fields['contact_person'].queryset = Company_contact_details.objects.none()

        if 'company' in self.data:
            try:
                # Ensure category_id is valid and not empty
                company_id = str(self.data.get('company'))
                self.fields['contact_person'].queryset = Company_contact_details.objects.filter(company_id=company_id)
            except (ValueError, TypeError):
                self.fields['contact_person'].queryset = Company_contact_details.objects.none()
        elif self.instance.pk:  # When editing an existing booking
            # Ensure that the instance has a valid category
            if self.instance.company:
                self.fields['contact_person'].queryset = Company_contact_details.objects.filter(company=self.instance.company)
            else:
                self.fields['contact_person'].queryset = Company_contact_details.objects.none()
            
    
        
        
        
        


class booking_trip_form(forms.ModelForm):
    class Meta:
        model=Booking_Trip_details
        exclude=['booking','booking_trip_id','is_deleted']
        
        widgets={
                'guest_name': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder':'Enter Guest Fullname',
                    'required':'required'
                }),
                'email': forms.EmailInput(attrs={
                    'class': 'form-control',
                    'placeholder':'Enter Guest Email ID'
                }),
                'contact_number': forms.NumberInput(attrs={
                    'class': 'form-control',
                    'placeholder':'Enter Conatct No :',
                    'required':'required'
                }),
                'whatsapp_number': forms.NumberInput(attrs={
                    'class': 'form-control',
                    'placeholder':'Enter Whatsapp No :'
                }),
                'supplier': forms.Select(attrs={
                    'class': 'form-select',
                    'style': 'background-color: transparent; border: none; border-bottom: 2px solid #D3D3D3; border-radius: 0;',
                    'required':'required'
                }),
                'category': forms.Select(attrs={
                    'class': 'form-select',
                    'style': 'background-color: transparent; border: none; border-bottom: 2px solid #D3D3D3; border-radius: 0;',
                    'required':'required'

                }),
                'package': forms.Select(attrs={
                    'class': 'form-select',
                    'style': 'background-color: transparent; border: none; border-bottom: 2px solid #D3D3D3; border-radius: 0;',
                    'required':'required'
                }),
                'trip_date': forms.DateInput(attrs={
                    'class': 'form-control',
                    'type':'date',
                    'required':'required'
                }),
                'trip_time': forms.TimeInput(attrs={
                    'class': 'form-control',
                    'type':'time',
                    'required':'required'
                }),
                'no_of_adult': forms.NumberInput(attrs={
                    'class': 'form-control',
                    'placeholder':'Enter No : of Adult',
                    'required':'required'

                }),
                'no_of_child': forms.NumberInput(attrs={
                    'class': 'form-control',
                    'placeholder':'Enter No : of Child',
                    'required':'required'
                }),
                'no_of_infant': forms.NumberInput(attrs={
                    'class': 'form-control',
                    'placeholder':'Enter No : of Infant',
                    'required':'required'
                }),
                'rate_of_adult': forms.NumberInput(attrs={
                    'class': 'form-control',
                    'placeholder':'Enter Rate of Adult',
                    'required':'required'
                }),
                
                 'rate_of_child': forms.NumberInput(attrs={
                    'class': 'form-control',
                    'placeholder':'Enter Rate of Child',
                    'required':'required'
                }),
                'rate_of_infant': forms.NumberInput(attrs={
                    'class': 'form-control',
                    'placeholder':'Enter Rate of Infant',
                    'required':'required'
                }),
                'remark': forms.Textarea(attrs={
                    'class': 'form-control',
                    'placeholder':'Enter Remark',
                    'style': 'height:75px !important;' 

                }),

                'room_no': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder':'Enter Room No :'
                }),
                'pickup_location': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder':'Enter Pickup Location'
                }),
                'pickup_time': forms.TimeInput(attrs={
                    'class': 'form-control',
                    'type':'time',
                }),
                'drop_location': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder':'Enter Drop off Location'
                }),
                'transfer_type': forms.Select(attrs={
                    'class': 'form-select',
                    'style': 'background-color: transparent; border: none; border-bottom: 2px solid #D3D3D3; border-radius: 0;',
                }),
                'vehicle_type': forms.Select(attrs={
                    'class': 'form-select',
                    'style': 'background-color: transparent; border: none; border-bottom: 2px solid #D3D3D3; border-radius: 0;',
                }),
                'vehicle_name': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder':'Enter Vehicle Name'
                }),
                'no_of_luggage': forms.NumberInput(attrs={
                    'class': 'form-control',
                    'placeholder':'Enter No : Luggage'
                }),
                'flight_time': forms.TimeInput(attrs={
                    'class': 'form-control',
                    'type':'time'
                }),
         }
        
        
def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    # Initialize the package queryset as empty by default
    self.fields['package'].queryset = Package.objects.none()

    if 'category' in self.data:
        try:
            # Ensure category_id is valid and not empty
            category_id = str(self.data.get('category'))
            self.fields['package'].queryset = Package.objects.filter(package_category_id=category_id)
        except (ValueError, TypeError):
            self.fields['package'].queryset = Package.objects.none()
    elif self.instance.pk:  # When editing an existing booking
        # Ensure that the instance has a valid category
        if self.instance.category:
            self.fields['package'].queryset = Package.objects.filter(package_category=self.instance.category)
        else:
            self.fields['package'].queryset = Package.objects.none()

  
    
    

            
    



booking_trip_formset=inlineformset_factory(
    Booking,Booking_Trip_details,form=booking_trip_form,extra=1,can_delete=False
)


edit_booking_trip_formset=inlineformset_factory(
    Booking,Booking_Trip_details,form=booking_trip_form,extra=0,can_delete=False
)


class Booking_filter_form(forms.Form):
    date_from=forms.DateField(
         required=False,
         widget=forms.DateInput(attrs={
            'type': 'date',  # This makes it a date picker
            'class': 'form-control',  # Add Bootstrap classes for styling
            
        })
    )
    date_to=forms.DateField(
         required=False,
         widget=forms.DateInput(attrs={
            'type': 'date',  # This makes it a date picker
            'class': 'form-control',  # Add Bootstrap classes for styling
            
        })
    )
    category=forms.ModelChoiceField(
          queryset=Category.objects.all(),
          required=False,
          widget=forms.Select(attrs={
            'class': 'form-select mt-1',
            'style': 'background-color: transparent; border: none; border-bottom: 2px solid #D3D3D3; border-radius: 0;',

        })                    
    )
    package=forms.ModelChoiceField(
          queryset=Package.objects.filter(is_deleted=False),
          required=False,
          widget=forms.Select(attrs={
            'class': 'form-select mt-1',
            'style': 'background-color: transparent; border: none; border-bottom: 2px solid #D3D3D3; border-radius: 0;',
        })                    
    )
    customer=forms.ModelChoiceField(
          queryset=Company.objects.filter(is_deleted=False),
          required=False,                   
          widget=forms.Select(attrs={
            'class': 'form-select mt-1',
            'style': 'background-color: transparent; border: none; border-bottom: 2px solid #D3D3D3; border-radius: 0;',
        })                    
    )
    payment_mode=forms.ModelChoiceField(
         queryset=Payment_mode.objects.all(),
          required=False,                       
          widget=forms.Select(attrs={
            'class': 'form-select mt-1',
            'style': 'background-color: transparent; border: none; border-bottom: 2px solid #D3D3D3; border-radius: 0;',
        })                    
    )
    payment_status=forms.ChoiceField(
          choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')],
          required=False, 
          initial=None,                        
          widget=forms.Select(attrs={
            'class': 'form-select mt-1',
            'style': 'background-color: transparent; border: none; border-bottom: 2px solid #D3D3D3; border-radius: 0;',
        })                    
    )
    status=forms.ModelChoiceField(
        queryset=Status_type.objects.all(),
          required=False,                 
          widget=forms.Select(attrs={
            'class': 'form-select mt-1',
            'style': 'background-color: transparent; border: none; border-bottom: 2px solid #D3D3D3; border-radius: 0;',

        })                    
    )
    booked_by=forms.CharField(max_length=100,
          required=False,                    
          widget=forms.Select(attrs={
            'class': 'form-control',  # Add Bootstrap classes for styling
            'required':False
        })                    
    )
    supplier=forms.ModelChoiceField(
          queryset=Supplier.objects.filter(is_deleted=False),                 
          required=False,                          
          widget=forms.Select(attrs={
            'class': 'form-select mt-1',
            'style': 'background-color: transparent; border: none; border-bottom: 2px solid #D3D3D3; border-radius: 0;',
        })                    
    )
    
    
    
    
class Supplier_filter_form(forms.Form):
    
    supplier_type=forms.ModelChoiceField(
          queryset=Supplier_type.objects.all(),
          required=False,
          widget=forms.Select(attrs={
            'class': 'form-select mt-1',
            'style': 'background-color: transparent; border: none; border-bottom: 2px solid #D3D3D3; border-radius: 0;',

        })                    
    )
    category=forms.ModelChoiceField(
          queryset=Category.objects.all(),
          required=False,
          widget=forms.Select(attrs={
            'class': 'form-select mt-1',
            'style': 'background-color: transparent; border: none; border-bottom: 2px solid #D3D3D3; border-radius: 0;',
        })                    
    )
    status=forms.ModelChoiceField(
          queryset=Status_type.objects.all(),
          required=False,                   
          widget=forms.Select(attrs={
            'class': 'form-select mt-1',
            'style': 'background-color: transparent; border: none; border-bottom: 2px solid #D3D3D3; border-radius: 0;',
        })                    
    )
   
    
    
    
