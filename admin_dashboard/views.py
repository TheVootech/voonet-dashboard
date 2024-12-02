from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import *
from .models import *
from django.views.generic.edit import UpdateView
from django.http import JsonResponse,HttpResponse
from django.template.loader import render_to_string
from django.middleware.csrf import get_token

def dashboard_view(request):
    return render(request,'dashboard.html')


def addbooking_view(request):
    return render(request,'addbooking.html')


def viewbooking_view(request):
    return render(request,'viewbooking.html')

def viewdriverallocation_view(request):
    return render(request,'viewdriverallocation.html')

def view_jobcard_view(request):
    return render (request,'viewjobcard.html')

def view_booking_report_view(request):
    return render (request,'view_booking_report.html')

def view_jobreport_view(request):
    return render(request,'view_jobreport.html')


def addpackages_view(request):
    if request.method=='POST':
        image=request.FILES.getlist("image")
        Hero_images=request.FILES.getlist("image")
        videos=request.FILES.getlist("video")
        form=Package_form(request.POST)
        
        if form.is_valid():
            package=form.save(commit=False)
            package.save()
            
            for i in image:
                Package_images.objects.create(package=package,image=i)
                
            for i in Hero_images:
                Hero_image.objects.create(package=package,image=i)
                
            for i in videos:
                Video.objects.create(package=package,video=i)
                
            messages.success(request,"New Package Added Successfully...")
            return redirect('add_package')
        else:
            messages.warning(request,"Package Adding Failed")
            return redirect('add_package')
    else:
        form=Package_form()
        imageform=Package_image_form()
        hero_image_form=Hero_image_form()
        video_form=Video_form()
    return render(request,'addpackages.html',{'form':form,'imageform':imageform,'heroimageform':hero_image_form,'videoform':video_form})


def addcategory_view(request):
    try:
        if request.method=='POST':
            form=Category_form(request.POST)
            if form.is_valid():
                form.save()
                data=Category.objects.all().values('category_id', 'category_name')
                category_list=list(data)
                return JsonResponse({'success':True,'category':category_list})
            else:
                return JsonResponse({'successs':False,'errors':form.errors})
        else:
            form=Category_form()
            data=Category.objects.all()
            return render(request,'addcategory.html',{'form':form,'data':data})
    except Exception as e:
        return JsonResponse({'success':False,'error':str(e)},status=500)
    




def addlanguage_view(request):
    try:
        if request.method == 'POST':
            form = Languages_form(request.POST)
            if form.is_valid():
                form.save()
                languages = Language.objects.all().values('language_id', 'language_name')
                language_list = list(languages)
                return JsonResponse({'success': True, 'languages': language_list})
            else:
                return JsonResponse({'success': False, 'errors': form.errors})
        else:
            form = Languages_form()
            languages = Language.objects.all()
        return render(request, 'addlanguage.html', {'form': form, 'data': languages})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)

    
    
    


def addsupplier_view(request):
    if request.method == 'POST':
        form = Supplier_form(request.POST)
        formset = Contact_details_formset(request.POST)

        # Check if both the form and the formset are valid
        if form.is_valid() and formset.is_valid():
            # Save the supplier form
            supplier = form.save(commit=False)
            supplier.save()

            # Associate the formset with the supplier
            formset.instance = supplier

            # Save the contact details in the formset
            formset.save()

            # Provide success feedback
            print(request.POST)
            return JsonResponse({'success':True})
        else:
            return JsonResponse({'success':False,'errors':form.errors})
   
    else:
        # For GET request, create empty forms
        form = Supplier_form()
        formset = Contact_details_formset()  # Use empty queryset to avoid initial extra forms

    return render(request, 'addsupplier.html', {'form': form, 'formset': formset})

    
    
    
def Supplier_allocation_view(request):
    data=Supplier_allocation.objects.all()
    form=Edit_allocate_supplier_form()
    return render(request,'supplierallocation.html',{'data':data,'form':form})


def Supplier_view(request):
    data=Supplier.objects.all()
    return render(request,'view_supplier.html',{'data':data})


def Allocate_new_supplier_view(request):
    try:
        if request.method=='POST':
            form=Allocate_supplier_form(request.POST)
            if form.is_valid():
                form.save()
                packages_without_suppliers = Package.objects.filter(supplier_allocation__isnull=True)
                newform=Allocate_supplier_form()
                new_form_html = render_to_string('partials/supplierallocateformajax.html', {'form': newform,'packagelength':packages_without_suppliers,'csrf_token': get_token(request),})
                return JsonResponse({'success': True, 'new_form_html': new_form_html})
            else:
                return JsonResponse({'success': False, 'errors': form.errors})
        else:
            packages_without_suppliers = Package.objects.filter(supplier_allocation__isnull=True)
            form=Allocate_supplier_form()
            return render(request,'add_supplier_allocation.html',{'form':form,'packagelength':packages_without_suppliers})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)
        
        
    
    
def Edit_supplier_allocation_view(request, pk):
    data = get_object_or_404(Supplier_allocation, pk=pk)
    
    if request.method == 'POST':
        form = Edit_allocate_supplier_form(request.POST, instance=data)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Supplier Allocation Edited Successfully")
            
            # If it's an AJAX request, return updated table as JSON
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                # Fetch all supplier allocation data and render the updated table
                all_data = Supplier_allocation.objects.all()  # or you can filter as needed
                updated_table_html = render_to_string('partials/supplier_allocation_table.html', {'data': all_data})
                
                return JsonResponse({'status': 'success', 'updated_table_html': updated_table_html})
            
            return redirect('supplier_allocation')  # Fallback if not AJAX
        
        else:
            messages.error(request, 'Supplier Allocation Editing Failed')
            return JsonResponse({'status': 'error', 'message': 'Form is invalid'}, status=400)

    else:
        form = Edit_allocate_supplier_form(instance=data)
        form_html = render_to_string('partials/editsupplierallocationform.html', {'form': form, 'csrf_token': get_token(request)})
        return JsonResponse({'form_html': form_html})
    
    

def Delete_supplier_allocation_view(request,pk):
    data=get_object_or_404(Supplier_allocation,pk=pk)
    if request.method=='POST':
        if data:
            data.delete()
            messages.success(request,'Item Deleted Successfully ')
            return redirect('supplier_allocation')
        else:
            messages.error(request,'Delete Failed,No Item Found ')
            return redirect('supplier_allocation')
    else:
        return render(request,'delete_supllier_allocation.html',{'data':data})
    
    



def deletesupplierallocation_view(request,pk):
    if request.method=='POST':
        try:
            data=Supplier_allocation.objects.get(id=pk)
            data.delete()
            all_data = Supplier_allocation.objects.all()  # or you can filter as needed
            updated_table_html = render_to_string('partials/supplier_allocation_table.html', {'data': all_data})
            
            return JsonResponse({'status': 'success', 'updated_table_html': updated_table_html})
        
        except Supplier_allocation.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Item not found'})
        
        
def supplier_details_view(request,pk):
    supplier=Supplier.objects.get(supplier_id=pk)
    contactperson=Contact_details.objects.filter(supplier=supplier)
    return render(request,'supplier_detailview.html',{'data':supplier,'contact':contactperson})





def edit_supplier_view(request, pk):
    # Retrieve the supplier object based on the pk
    supplier = Supplier.objects.get(supplier_id=pk)

    if request.method == 'POST':
        form = Supplier_form(request.POST,instance=supplier)
        formset = Contact_details_formset(request.POST,instance=supplier)

        # Check if both the form and the formset are valid
        if form.is_valid() and formset.is_valid():
            # Save the supplier form
            editdata = form.save(commit=False)
            editdata.save()

            # Associate the formset with the supplier
            formset.instance = editdata

            # Save the contact details in the formset
            formset.save()

            # Provide success feedback
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                # Fetch all supplier allocation data and render the updated table
                all_data = Supplier.objects.all()  # or you can filter as needed
                updated_table_html = render_to_string('partials/suppliertable.html', {'data': all_data})
                
                return JsonResponse({'status': 'success', 'updated_table_html': updated_table_html})
            
            return redirect('supplier_allocation') # Ensure 'add_supplier' is the correct URL name

        else:
            # Provide warning feedback if any form or formset is invalid
            messages.warning(request, "Supplier Adding Failed...")
            print(form.errors)
            print(formset.errors)
    
    else:
        # For GET request, create empty forms
        form = Supplier_form(instance=supplier)
        formset = Contact_details_formset(instance=supplier) 

    return render(request, 'editsupplier.html', {'form': form, 'formset': formset, 'supplier': supplier})
    


def update_supplier_view(request, pk):
    try:
        # Fetch the supplier instance to update
        supplier = Supplier.objects.get(pk=pk)
    except Supplier.DoesNotExist:
        messages.error(request, 'Supplier does not exist.')
        return redirect('supplier')  # Ensure 'supplier_list' is the correct URL name

    if request.method == 'POST':
        form = Supplier_form(request.POST, instance=supplier)
        formset = Contact_details_formset(request.POST, instance=supplier)

        # Check if both the form and the formset are valid
        if form.is_valid() and formset.is_valid():
            # Save the supplier form
            supplier = form.save(commit=False)
            supplier.save()

            # Associate the formset with the supplier
            formset.instance = supplier

            # Save the contact details in the formset
            formset.save()

            # Provide success feedback
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                # Fetch all supplier allocation data and render the updated table
                all_data = Supplier.objects.all()  # or you can filter as needed
                updated_table_html = render_to_string('partials/suppliertable.html', {'data': all_data})
                
                return JsonResponse({'status': 'success', 'updated_table_html': updated_table_html})
            
            return redirect('supplier')  # Ensure 'supplier_list' is the correct URL name

        else:
            # Provide warning feedback if any form or formset is invalid
            messages.warning(request, 'Updating supplier failed.')
            print(form.errors)
            print(formset.errors)
    
    else:
        # For GET request, populate the forms with existing data
        form = Supplier_form(instance=supplier)
        formset = Contact_details_formset(instance=supplier)
        form_html = render_to_string('partials/editsupplier.html', {'form': form,'formset':formset, 'csrf_token': get_token(request)})
        return JsonResponse({'form_html': form_html})



def delete_supplier_view(request,pk):
    
    if request.method=='POST':
        try:
            data=Supplier.objects.get(pk=pk)
            data.delete()
            all_data = Supplier.objects.all()  # or you can filter as needed
            updated_table_html = render_to_string('partials/suppliertable.html', {'data': all_data})
            
            return JsonResponse({'status': 'success', 'updated_table_html': updated_table_html})
        except Supplier.DoesNotExist:
            return JsonResponse({'status':'error','message':'item not found'})
        
        
        

def addcompany_view(request):
    if request.method == 'POST':
        form = Company_form(request.POST,request.FILES)
        formset = Company_contact_details_formset(request.POST)

        # Check if both the form and the formset are valid
        if form.is_valid() and formset.is_valid():
            # Save the supplier form
            company = form.save(commit=False)
            company.save()

            # Associate the formset with the supplier
            formset.instance = company

            # Save the contact details in the formset
            formset.save()

            # Provide success feedback
            print(request.POST)
            return JsonResponse({'success':True})
        else:
            print(formset.errors)
            return JsonResponse({'success':False,'errors':form.errors})
   
    else:
        # For GET request, create empty forms
        form = Company_form()
        formset = Company_contact_details_formset()  # Use empty queryset to avoid initial extra forms

    return render(request, 'addcompany.html', {'form': form, 'formset': formset})




def view_company(request):
    data=Company.objects.all()
    return render(request,'viewcompany.html',{'data':data})




def company_detail_view(request,pk):
    company=Company.objects.get(company_id=pk)
    contact=Company_contact_details.objects.filter(company=company)
    return render(request,'company_detailview.html',{'data':company,'contact':contact})


def edit_company_view(request,pk):
    try:
        company=Company.objects.get(pk=pk)
    except Company.DoesNotExist:
        messages.error(request,'Company Does not exist')
        return redirect('company')
    
    if request.method == 'POST':
        form=Company_form(request.POST,request.FILES,instance=company)
        formset=Company_contact_details_formset(request.POST,instance=company)
        
        if form.is_valid() and formset.is_valid():
            
            company=form.save(commit=False)
            company.save()
            formset.instance=company
            formset.save()
            
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                
                all_data = Company.objects.all()
                updated_table_html=render_to_string('partials/companytable.html',{'data':all_data})
                return JsonResponse({'status': 'success', 'updated_table_html': updated_table_html})
            
            return redirect('company')
        
        else:
                # Provide warning feedback if any form or formset is invalid
                messages.warning(request, 'Updating company failed.')
                print(form.errors)
                print(formset.errors)
    
    else:
        form = Company_form(instance=company)
        formset = Company_contact_details_formset(instance=company)
        form_html = render_to_string('partials/editcompany.html', {'form': form,'formset':formset, 'csrf_token': get_token(request)})
        return JsonResponse({'form_html': form_html})
            
            
            
def delete_company_view(request,pk):
   
    if request.method == 'POST':
        try:
            data=Company.objects.get(pk=pk)
            data.delete()
            all_data=Company.objects.all()
            updated_table_html=render_to_string('partials/companytable.html',{'data':all_data})
            
            return JsonResponse({'status':'success','updated_table_html':updated_table_html})
        
        except Company.DoesNotExist:
            return JsonResponse({'status':'error','message':'item not found'})