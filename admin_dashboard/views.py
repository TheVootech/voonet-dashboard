from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import *
from .models import *
from django.views.generic.edit import UpdateView
from django.http import JsonResponse,HttpResponse
from django.template.loader import render_to_string
from django.middleware.csrf import get_token
from django.utils import timezone
import json

def dashboard_view(request):
    return render(request,'dashboard.html')

def get_contact_persons(request):
    company_id = request.GET.get('company_id')
    contact_persons = Company_contact_details.objects.filter(company=company_id).values('id', 'name','designation')
    return JsonResponse(list(contact_persons), safe=False)


def get_package(request):
    category_id = request.GET.get('category_id')
    package = Package.objects.filter(package_category=category_id).values('package_id', 'package_title')
    return JsonResponse(list(package), safe=False)





def viewbooking_view(request):
    return render(request,'viewbooking.html')

def viewdriverallocation_view(request):
    data=Booking_Trip_details.objects.filter(is_deleted=False)
    return render(request,'viewdriverallocation.html',{'data':data,'form':Booking_filter_form,'assignform':Assign_form})

def assign_driver_guide_supplier(request):
    if request.method == 'POST':
        try:
            print(request.body)
            # Get the list of booking_trip_ids from the request
            data = json.loads(request.body)
            booking_trip_ids = data.get('booking_trip_ids', [])
            driver_id=data.get('driver_id')
            guide_id=data.get('guide_id')
            supplier_id=data.get('supplier_id')
            
            
            driver = Driver.objects.get(driver_id=driver_id) if driver_id else None
            guide = Guide.objects.get(guide_id=guide_id) if guide_id else None
            supplier = Supplier.objects.get(supplier_id=supplier_id) if supplier_id else None

            for trip_id in booking_trip_ids:
                try:
                    trip=Booking_Trip_details.objects.get(booking_trip_id=trip_id)
                    
                    if driver:
                        trip.driver=driver
                    if guide:
                        trip.guide=guide
                    if supplier:
                        trip.supplier=supplier
                        
                    trip.save()
                    
                except trip.DoesNotExist:
                    messages.error(request, 'Booking does not exist.')
                    return redirect('viewdriverallocation') 
                    

            updated_table_html = render_to_string('partials/driverallocationtable.html', {
            'data': Booking_Trip_details.objects.filter(is_deleted=False) ,'assignform' :Assign_form
        })

            # Return a success response with the updated table HTML
            return JsonResponse({
                'status': 'success',
                'updated_table_html': updated_table_html
            })

        except (Driver.DoesNotExist, Guide.DoesNotExist, Supplier.DoesNotExist) as e:
            # Handle the case where any of the referenced objects (driver, guide, supplier) do not exist
            return JsonResponse({'status': 'error', 'message': str(e)})

        except Exception as e:
            # Handle any unexpected error
            return JsonResponse({'status': 'error', 'message': 'An error occurred: ' + str(e)})

    else:
        # Return an error if the request is not POST
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})
    


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
            form.save_m2m()
            
            for i in image:
                Package_images.objects.create(package=package,image=i)
                
            for i in Hero_images:
                Hero_image.objects.create(package=package,image=i)
                
            for i in videos:
                Video.objects.create(package=package,video=i)
                
            return JsonResponse({'success':True})
        else:
            return JsonResponse({'success':False,'errors':form.errors})
    else:
        form=Package_form()
        imageform=Package_image_form()
        hero_image_form=Hero_image_form()
        video_form=Video_form()
    return render(request,'addpackages.html',{'form':form,'imageform':imageform,'heroimageform':hero_image_form,'videoform':video_form})


def view_package(request):
    data=Package.objects.filter(is_deleted=False)
    return render(request,'viewpackage.html',{'data':data,'form':Package_filter_form})



def filter_Package(request):
    form = Package_filter_form(request.GET)  # Initialize the form with GET data
    package = Package.objects.filter(is_deleted=False)


    if form.is_valid():
        category = form.cleaned_data.get('category')
        sunday = form.cleaned_data.get('sunday')
        monday = form.cleaned_data.get('monday')
        tuesday = form.cleaned_data.get('tuesday')
        wednesday = form.cleaned_data.get('wednesday')
        thursday = form.cleaned_data.get('thursday')
        friday = form.cleaned_data.get('friday')
        saturday = form.cleaned_data.get('saturday')
        transportation = form.cleaned_data.get('transportation')
        status = form.cleaned_data.get('status')
        

        if category:
            package = package.filter(package_category=category)
            
        if sunday:
            package = package.filter(sunday=True)
            
        if monday:
            package = package.filter(monday=True)
            
        if tuesday:
            package = package.filter(tuesday=True)
            
        if wednesday:
            package = package.filter(wednesday=True)
            
        if thursday:
            package = package.filter(thursday=True)
            
        if friday:
            package = package.filter(friday=True)
            
        if saturday:
            package = package.filter(saturday=True)
            
        if not sunday and not monday and not tuesday and not wednesday and not thursday and not friday and not saturday:
            package = package
            
        if transportation and transportation != '______':
            package = package.filter(transportation=transportation)
            
        if status:
            package = package.filter(status=status)
        

    # Render the updated table as a partial HTML
    bookings_html = render_to_string('partials/package_table.html', {'data':package})

    # Return the HTML as a response
    return JsonResponse({'status': 'success', 'bookings_html': bookings_html})


def package_detail_view(request,pk):
    data=Package.objects.get(pk=pk)
    return render(request,'package_detail_view.html',{'data':data})





def edit_package_view(request,pk):
    try:
        # Fetch the supplier instance to update
        package = Package.objects.get(pk=pk)
    except Package.DoesNotExist:
        messages.error(request, 'Package does not exist.')
        return redirect('viewpackage')  # Ensure 'supplier_list' is the correct URL name

    if request.method == 'POST':
        image=request.FILES.getlist("image")
        Hero_images=request.FILES.getlist("image")
        videos=request.FILES.getlist("video")
        form=Package_form(request.POST,instance=package)

        # Check if both the form and the formset are valid
        if form.is_valid():
            package=form.save(commit=False)
            package.save()
            
            for i in image:
                Package_images.objects.create(package=package,image=i)
                
            for i in Hero_images:
                Hero_image.objects.create(package=package,image=i)
                
            for i in videos:
                Video.objects.create(package=package,video=i)
           
            
            # Provide success feedback
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                # Fetch all supplier allocation data and render the updated table
                all_data = Package.objects.all()  # or you can filter as needed
                updated_table_html = render_to_string('partials/package_table.html', {'data': all_data})
                
                return JsonResponse({'status': 'success', 'updated_table_html': updated_table_html})
            
            return redirect('viewpackage')  # Ensure 'supplier_list' is the correct URL name

        else:
            # Provide warning feedback if any form or formset is invalid
            messages.warning(request, 'Updating package failed.')
            print(form.errors)
    
    else:
        # For GET request, populate the forms with existing data
        form=Package_form(instance=package)
        imageform=Package_image_form(instance=package)
        hero_image_form=Hero_image_form(instance=package)
        video_form=Video_form(instance=package)
        form_html = render_to_string('partials/editpackage.html', {'form':form,'imageform':imageform,'heroimageform':hero_image_form,'videoform':video_form,'csrf_token': get_token(request)})
        return JsonResponse({'form_html': form_html})
    
    
    
def delete_package_view(request,pk):
    if request.method == 'POST' :
        try:
            data=Package.objects.get(pk=pk)
            data.is_deleted = True
            data.save()
            
            all_data=Package.objects.filter(is_deleted=False)
            updated_table_html=render_to_string('partials/package_table.html',{'data':all_data})
            return JsonResponse({'status':'success','updated_table_html':updated_table_html})
        
        except Package.DoesNotExist:
            return JsonResponse({'status':'error','message':'item not found'})
        
        
def delete_package_forever_view(request,pk):
    if request.method == 'POST' :
        try:
            data=Package.objects.get(pk=pk)
            data.delete()
            all_data=Package.objects.filter(is_deleted=True)
            updated_table_html=render_to_string('partials/package_trash_table.html',{'data':all_data})
            return JsonResponse({'status':'success','updated_table_html':updated_table_html})
        
        except Package.DoesNotExist:
            return JsonResponse({'status':'error','message':'item not found'})
        
        
def recover_package_view(request,pk):
    if request.method == 'POST' :
        try:
            data=Package.objects.get(pk=pk)
            data.is_deleted = False
            data.save()
            
            all_data=Package.objects.filter(is_deleted=True)
            updated_table_html=render_to_string('partials/package_trash_table.html',{'data':all_data})
            return JsonResponse({'status':'success','updated_table_html':updated_table_html})
        
        except Package.DoesNotExist:
            return JsonResponse({'status':'error','message':'item not found'})
        
        
def view_package_trash(request):
    data=Package.objects.filter(is_deleted=True)
    return render(request,'packagetrash.html',{'data':data})


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
    
    
def View_category(request):
    data=Category.objects.all()
    return render(request,'view_category.html',{'data':data})


def edit_category_view(request,pk):
    try:
        # Fetch the supplier instance to update
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        messages.error(request, 'Category does not exist.')
        return redirect('view_category')  # Ensure 'supplier_list' is the correct URL name

    if request.method == 'POST':
        form = Category_form(request.POST, instance=category)

        # Check if both the form and the formset are valid
        if form.is_valid():
            # Save the supplier form
            category = form.save(commit=False)
            category.save()

            # Associate the formset with the supplier
            
            # Provide success feedback
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                # Fetch all supplier allocation data and render the updated table
                all_data = Category.objects.all()  # or you can filter as needed
                updated_table_html = render_to_string('partials/category_table.html', {'data': all_data})
                
                return JsonResponse({'status': 'success', 'updated_table_html': updated_table_html})
            
            return redirect('view_category')  # Ensure 'supplier_list' is the correct URL name

        else:
            # Provide warning feedback if any form or formset is invalid
            messages.warning(request, 'Updating category failed.')
            print(form.errors)
    
    else:
        # For GET request, populate the forms with existing data
        form = Category_form(instance=category)
        form_html = render_to_string('partials/editcategory.html', {'form': form,'csrf_token': get_token(request)})
        return JsonResponse({'form_html': form_html})
    
    
    
def delete_category_view(request,pk):
    if request.method == 'POST' :
        try:
            data=Category.objects.get(pk=pk)
            data.delete()
            
            all_data=Category.objects.all()
            updated_table_html=render_to_string('partials/category_table.html',{'data':all_data})
            return JsonResponse({'status':'success','updated_table_html':updated_table_html})
        
        except Category.DoesNotExist:
            return JsonResponse({'status':'error','message':'item not found'})




           




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

    
    
def View_language(request):
    data=Language.objects.all()
    return render(request,'view_language.html',{'data':data})



def edit_language_view(request,pk):
    try:
        # Fetch the supplier instance to update
        language = Language.objects.get(pk=pk)
    except Language.DoesNotExist:
        messages.error(request, 'Language does not exist.')
        return redirect('viewlanguage')  # Ensure 'supplier_list' is the correct URL name

    if request.method == 'POST':
        form = Languages_form(request.POST, instance=language)

        # Check if both the form and the formset are valid
        if form.is_valid():
            # Save the supplier form
            language = form.save(commit=False)
            language.save()

            # Associate the formset with the supplier
            
            # Provide success feedback
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                # Fetch all supplier allocation data and render the updated table
                all_data = Language.objects.all()  # or you can filter as needed
                updated_table_html = render_to_string('partials/language_table.html', {'data': all_data})
                
                return JsonResponse({'status': 'success', 'updated_table_html': updated_table_html})
            
            return redirect('viewlanguage')  # Ensure 'supplier_list' is the correct URL name

        else:
            # Provide warning feedback if any form or formset is invalid
            messages.warning(request, 'Updating language failed.')
            print(form.errors)
    
    else:
        # For GET request, populate the forms with existing data
        form = Languages_form(instance=language)
        form_html = render_to_string('partials/editlanguage.html', {'form': form,'csrf_token': get_token(request)})
        return JsonResponse({'form_html': form_html})



def delete_language_view(request,pk):
    if request.method == 'POST' :
        try:
            data=Language.objects.get(pk=pk)
            data.delete()
            
            all_data=Language.objects.all()
            updated_table_html=render_to_string('partials/language_table.html',{'data':all_data})
            return JsonResponse({'status':'success','updated_table_html':updated_table_html})
        
        except Category.DoesNotExist:
            return JsonResponse({'status':'error','message':'item not found'})


def addsupplier_view(request):
    if request.method == 'POST':
        form = Supplier_form(request.POST,request.FILES)
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
    data=Supplier_allocation.objects.all().order_by('package')
    form=Edit_allocate_supplier_form()
    return render(request,'supplierallocation.html',{'data':data,'form':form})


def Supplier_view(request):
    data=Supplier.objects.filter(is_deleted=False) 
    return render(request,'view_supplier.html',{'data':data,'form':Supplier_filter_form})



def filter_Supplier(request):
    form = Supplier_filter_form(request.GET)  # Initialize the form with GET data
    supplier = Supplier.objects.filter(is_deleted=False)


    if form.is_valid():
        type = form.cleaned_data.get('supplier_type')
        category = form.cleaned_data.get('category')
        status = form.cleaned_data.get('status')
        

        if type:
            supplier = supplier.filter(supplier_type=type)
        if category:
            supplier = supplier.filter(category__category_name__icontains=category)
        if status:
            supplier = supplier.filter(status=status)
        

    # Render the updated table as a partial HTML
    bookings_html = render_to_string('partials/suppliertable.html', {'data': supplier})

    # Return the HTML as a response
    return JsonResponse({'status': 'success', 'bookings_html': bookings_html})



def filter_Driver(request):
    form = Driver_filter_form(request.GET)  # Initialize the form with GET data
    driver = Driver.objects.filter(is_deleted=False)


    if form.is_valid():
        type = form.cleaned_data.get('driver_type')
        status = form.cleaned_data.get('status')
        

        if type and type != '______':
            driver = driver.filter(driver_type=type)
       
        if status:
            driver = driver.filter(status=status)
        

    # Render the updated table as a partial HTML
    bookings_html = render_to_string('partials/driver_table.html', {'data': driver})

    # Return the HTML as a response
    return JsonResponse({'status': 'success', 'bookings_html': bookings_html})



def filter_Guide(request):
    form = Guide_filter_form(request.GET)  # Initialize the form with GET data
    guide = Guide.objects.filter(is_deleted=False)


    if form.is_valid():
        abudhabi = form.cleaned_data.get('abudhabi_license')
        dubai = form.cleaned_data.get('dubai_license')
        rak = form.cleaned_data.get('rak_license')
        sharjah = form.cleaned_data.get('sharjah_license')
        fujairah = form.cleaned_data.get('fujairah_license')
        status = form.cleaned_data.get('status')
        

        if abudhabi:
            guide = guide.filter(abudhabi_license=True)
            
        if dubai:
            guide = guide.filter(dubai_license=True)
            
        if rak:
            guide = guide.filter(rak_license=True)
            
        if sharjah:
            guide = guide.filter(sharjah_license=True)
            
        if fujairah:
            guide = guide.filter(fujairah_license=True)
            
        if not abudhabi and not dubai and not rak and not sharjah and not fujairah:
            guide = guide
            
        if status:
            guide = guide.filter(status=status)
        

    # Render the updated table as a partial HTML
    bookings_html = render_to_string('partials/guide_table.html', {'data':guide})

    # Return the HTML as a response
    return JsonResponse({'status': 'success', 'bookings_html': bookings_html})








def Allocate_new_supplier_view(request):
    try:
        if request.method=='POST':
            form=Allocate_supplier_form(request.POST)
            if form.is_valid():
                form.save()
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'errors': form.errors})
        else:
            
            form=Allocate_supplier_form()
            return render(request,'add_supplier_allocation.html',{'form':form})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)
        
        
    
    
def Edit_supplier_allocation_view(request, pk):
    data = get_object_or_404(Supplier_allocation, pk=pk)
    
    if request.method == 'POST':
        form = form=Edit_allocate_supplier_form(request.POST, instance=data)
        
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
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)

    else:
        form = form=Edit_allocate_supplier_form(instance=data)
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
        form = Supplier_form(request.POST,request.FILES,instance=supplier)
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
        form = Supplier_form(request.POST,request.FILES,instance=supplier)
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
            data.is_deleted=True
            data.save()
            
            all_data = Supplier.objects.filter(is_deleted=False)  # or you can filter as needed
            updated_table_html = render_to_string('partials/suppliertable.html', {'data': all_data})
            
            return JsonResponse({'status': 'success', 'updated_table_html': updated_table_html})
        except Supplier.DoesNotExist:
            return JsonResponse({'status':'error','message':'item not found'})
        
        
def view_supplier_trash(request):
    data=Supplier.objects.filter(is_deleted=True)
    return render(request,'suppliertrash.html',{'data':data})

        
        
def recover_supplier_view(request,pk):
    if request.method == 'POST' :
        try:
            data=Supplier.objects.get(pk=pk)
            data.is_deleted = False
            data.save()
            
            all_data=Supplier.objects.filter(is_deleted=True)
            updated_table_html=render_to_string('partials/supplier_trash_table.html',{'data':all_data})
            return JsonResponse({'status':'success','updated_table_html':updated_table_html})
        
        except Package.DoesNotExist:
            return JsonResponse({'status':'error','message':'item not found'})
        

        
def delete_Supplier_forever_view(request,pk):
    if request.method == 'POST' :
        try:
            data=Supplier.objects.get(pk=pk)
            data.delete()
            all_data=Supplier.objects.filter(is_deleted=True)
            updated_table_html=render_to_string('partials/supplier_trash_table.html',{'data':all_data})
            return JsonResponse({'status':'success','updated_table_html':updated_table_html})
        
        except Company.DoesNotExist:
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
    data=Company.objects.filter(is_deleted=False)
    return render(request,'viewcompany.html',{'data':data,'form':Customer_filter_form})


def filter_Customer(request):
    form = Customer_filter_form(request.GET)  # Initialize the form with GET data
    customer = Company.objects.filter(is_deleted=False)


    if form.is_valid():
        type = form.cleaned_data.get('customer_type')
        status = form.cleaned_data.get('status')
        

        if type:
            customer = customer.filter(company_type=type)
            
        if status:
            customer = customer.filter(status=status)
        

    # Render the updated table as a partial HTML
    bookings_html = render_to_string('partials/companytable.html', {'data':customer})

    # Return the HTML as a response
    return JsonResponse({'status': 'success', 'bookings_html': bookings_html})




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
        formset=Edit_company_contact_details_formset(request.POST,instance=company)
        
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
        formset = Edit_company_contact_details_formset(instance=company)
        form_html = render_to_string('partials/editcompany.html', {'form': form,'formset':formset, 'csrf_token': get_token(request)})
        return JsonResponse({'form_html': form_html})
            
            
            
def delete_company_view(request,pk):
   
    if request.method == 'POST':
        try:
            data=Company.objects.get(pk=pk)
            data.is_deleted = True
            data.save()
            all_data=Company.objects.filter(is_deleted=False)
            updated_table_html=render_to_string('partials/companytable.html',{'data':all_data})
            
            return JsonResponse({'status':'success','updated_table_html':updated_table_html})
        
        except Company.DoesNotExist:
            return JsonResponse({'status':'error','message':'item not found'})
        
def view_company_trash(request):
    data=Company.objects.filter(is_deleted=True)
    return render(request,'companytrash.html',{'data':data})



def recover_company_view(request,pk):
    if request.method == 'POST' :
        try:
            data=Company.objects.get(pk=pk)
            data.is_deleted = False
            data.save()
            
            all_data=Company.objects.filter(is_deleted=True)
            updated_table_html=render_to_string('partials/company_trash_table.html',{'data':all_data})
            return JsonResponse({'status':'success','updated_table_html':updated_table_html})
        
        except Package.DoesNotExist:
            return JsonResponse({'status':'error','message':'item not found'})
        

        
def delete_company_forever_view(request,pk):
    if request.method == 'POST' :
        try:
            data=Company.objects.get(pk=pk)
            data.delete()
            all_data=Company.objects.filter(is_deleted=True)
            updated_table_html=render_to_string('partials/company_trash_table.html',{'data':all_data})
            return JsonResponse({'status':'success','updated_table_html':updated_table_html})
        
        except Company.DoesNotExist:
            return JsonResponse({'status':'error','message':'item not found'})

        
        
        
def addpaymentmode_view(request):
    try:
        if request.method == 'POST':
            form = Payment_form(request.POST)
            if form.is_valid():
                form.save()
                payments = Payment_mode.objects.all().values('payment_id', 'payment_mode')
                payment_list = list(payments)
                return JsonResponse({'success': True, 'payments': payment_list})
            else:
                return JsonResponse({'success': False, 'errors': form.errors})
        else:
            form = Payment_form()
            payments = Payment_mode.objects.all()
        return render(request, 'addpayment.html', {'form': form, 'data': payments})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)
    
    
    
def view_payment(request):
    data=Payment_mode.objects.all()
    return render(request,'viewpayment.html',{'data':data})



def edit_payment_view(request,pk):
    try:
        # Fetch the supplier instance to update
        payment = Payment_mode.objects.get(pk=pk)
    except payment.DoesNotExist:
        messages.error(request, 'payment does not exist.')
        return redirect('viewpayment')  # Ensure 'supplier_list' is the correct URL name

    if request.method == 'POST':
        form = Payment_form(request.POST, instance=payment)

        # Check if both the form and the formset are valid
        if form.is_valid():
            # Save the supplier form
            payment = form.save(commit=False)
            payment.save()

            # Associate the formset with the supplier
            
            # Provide success feedback
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                # Fetch all supplier allocation data and render the updated table
                all_data = Payment_mode.objects.all()  # or you can filter as needed
                updated_table_html = render_to_string('partials/payment_table.html', {'data': all_data})
                
                return JsonResponse({'status': 'success', 'updated_table_html': updated_table_html})
            
            return redirect('viewpayment')  # Ensure 'supplier_list' is the correct URL name

        else:
            # Provide warning feedback if any form or formset is invalid
            messages.warning(request, 'Updating payment failed.')
            print(form.errors)
    
    else:
        # For GET request, populate the forms with existing data
        form = Payment_form(instance=payment)
        form_html = render_to_string('partials/editpayment.html', {'form': form,'csrf_token': get_token(request)})
        return JsonResponse({'form_html': form_html})
    
    
    
def delete_payment_view(request,pk):
   
    if request.method == 'POST':
        try:
            data=Payment_mode.objects.get(pk=pk)
            data.delete()
            all_data=Payment_mode.objects.all()
            updated_table_html=render_to_string('partials/payment_table.html',{'data':all_data})
            
            return JsonResponse({'status':'success','updated_table_html':updated_table_html})
        
        except Payment_mode.DoesNotExist:
            return JsonResponse({'status':'error','message':'item not found'})
        
        
        
        
def adddriver_view(request):
    if request.method == 'POST':
        form = Driver_form(request.POST,request.FILES)

        # Check if both the form and the formset are valid
        if form.is_valid():
            # Save the supplier form
            company = form.save(commit=False)
            company.save()


            # Provide success feedback
            print(request.POST)
            return JsonResponse({'success':True})
        else:
            return JsonResponse({'success':False,'errors':form.errors})
   
    else:
        # For GET request, create empty forms
        form = Driver_form()

    return render(request, 'adddriver.html', {'form': form})


def view_driver(request):
    data=Driver.objects.filter(is_deleted=False)
    return render(request,'viewdriver.html',{'data':data,'form':Driver_filter_form})


def driver_details_view(request,pk):
    data=Driver.objects.get(driver_id=pk)
    return render(request,'driverdetailsview.html',{'data':data})



def edit_driver_view(request,pk):
    try:
        # Fetch the supplier instance to update
        driver = Driver.objects.get(pk=pk)
    except driver.DoesNotExist:
        messages.error(request, 'driver does not exist.')
        return redirect('viewdriver')  # Ensure 'supplier_list' is the correct URL name

    if request.method == 'POST':
        form = Driver_form(request.POST,request.FILES, instance=driver)

        # Check if both the form and the formset are valid
        if form.is_valid():
            # Save the supplier form
            driver = form.save(commit=False)
            driver.save()

            # Associate the formset with the supplier
            
            # Provide success feedback
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                # Fetch all supplier allocation data and render the updated table
                all_data = Driver.objects.all()  # or you can filter as needed
                updated_table_html = render_to_string('partials/driver_table.html', {'data': all_data})
                
                return JsonResponse({'status': 'success', 'updated_table_html': updated_table_html})
            
            return redirect('viewdriver')  # Ensure 'supplier_list' is the correct URL name

        else:
            # Provide warning feedback if any form or formset is invalid
            messages.warning(request, 'Updating driver failed.')
            print(form.errors)
    
    else:
        # For GET request, populate the forms with existing data
        form = Driver_form(instance=driver)
        form_html = render_to_string('partials/editdriver.html', {'form': form,'csrf_token': get_token(request)})
        return JsonResponse({'form_html': form_html})
    
    
    
    
def delete_driver_view(request,pk):
   
    if request.method == 'POST':
        try:
            data=Driver.objects.get(pk=pk)
            data.is_deleted=True
            data.save()
            
            all_data=Driver.objects.filter(is_deleted=False)
            updated_table_html=render_to_string('partials/driver_table.html',{'data':all_data})
            
            return JsonResponse({'status':'success','updated_table_html':updated_table_html})
        
        except Driver.DoesNotExist:
            return JsonResponse({'status':'error','message':'item not found'})
        
        
def view_driver_trash(request):
    data=Driver.objects.filter(is_deleted=True)
    return render(request,'drivertrash.html',{'data':data})

        
        
def recover_driver_view(request,pk):
    if request.method == 'POST' :
        try:
            data=Driver.objects.get(pk=pk)
            data.is_deleted = False
            data.save()
            
            all_data=Driver.objects.filter(is_deleted=True)
            updated_table_html=render_to_string('partials/driver_trash_table.html',{'data':all_data})
            return JsonResponse({'status':'success','updated_table_html':updated_table_html})
        
        except Driver.DoesNotExist:
            return JsonResponse({'status':'error','message':'item not found'})
        

        
def delete_driver_forever_view(request,pk):
    if request.method == 'POST' :
        try:
            data=Driver.objects.get(pk=pk)
            data.delete()
            all_data=Driver.objects.filter(is_deleted=True)
            updated_table_html=render_to_string('partials/driver_trash_table.html',{'data':all_data})
            return JsonResponse({'status':'success','updated_table_html':updated_table_html})
        
        except Driver.DoesNotExist:
            return JsonResponse({'status':'error','message':'item not found'})
        
        
def addguide_view(request):
    if request.method == 'POST':
        form = Guide_form(request.POST,request.FILES)

        # Check if both the form and the formset are valid
        if form.is_valid():
            # Save the supplier form
            form.save()


            # Provide success feedback
            print(request.POST)
            return JsonResponse({'success':True})
        else:
            return JsonResponse({'success':False,'errors':form.errors})
   
    else:
        # For GET request, create empty forms
        form = Guide_form()

    return render(request, 'addguide.html', {'form': form})



def view_guide(request):
    data=Guide.objects.filter(is_deleted=False)
    return render(request,'viewguide.html',{'data':data,'form':Guide_filter_form})




def guide_details_view(request,pk):
    data=Guide.objects.get(guide_id=pk)
    return render(request,'guidedetailsview.html',{'data':data})





def edit_guide_view(request,pk):
    try:
        # Fetch the supplier instance to update
        guide = Guide.objects.get(pk=pk)
    except guide.DoesNotExist:
        messages.error(request, 'guide does not exist.')
        return redirect('viewguide')  # Ensure 'supplier_list' is the correct URL name

    if request.method == 'POST':
        form = Guide_form(request.POST,request.FILES,instance=guide)

        # Check if both the form and the formset are valid
        if form.is_valid():
            # Save the supplier form
            form.save()

            # Provide success feedback
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                # Fetch all supplier allocation data and render the updated table
                all_data = Guide.objects.all()  # or you can filter as needed
                updated_table_html = render_to_string('partials/guide_table.html', {'data': all_data})
                
                return JsonResponse({'status': 'success', 'updated_table_html': updated_table_html})
            
            return redirect('viewguide')  # Ensure 'supplier_list' is the correct URL name

        else:
            # Provide warning feedback if any form or formset is invalid
            messages.warning(request, 'Updating guide failed.')
            print(form.errors)
    
    else:
        # For GET request, populate the forms with existing data
        form = Guide_form(instance=guide)
        form_html = render_to_string('partials/editguide.html', {'form': form,'csrf_token': get_token(request)})
        return JsonResponse({'form_html': form_html})
    
    
    
    
def delete_guide_view(request,pk):
   
    if request.method == 'POST':
        try:
            data=Guide.objects.get(pk=pk)
            data.is_deleted=True
            data.save()
            
            all_data=Guide.objects.filter(is_deleted=False)
            updated_table_html=render_to_string('partials/guide_table.html',{'data':all_data})
            
            return JsonResponse({'status':'success','updated_table_html':updated_table_html})
        
        except Guide.DoesNotExist:
            return JsonResponse({'status':'error','message':'item not found'})
        
        


def view_guide_trash(request):
    data=Guide.objects.filter(is_deleted=True)
    return render(request,'guidetrash.html',{'data':data})

        
        
def recover_guide_view(request,pk):
    if request.method == 'POST' :
        try:
            data=Guide.objects.get(pk=pk)
            data.is_deleted = False
            data.save()
            
            all_data=Guide.objects.filter(is_deleted=True)
            updated_table_html=render_to_string('partials/guide_trash_table.html',{'data':all_data})
            return JsonResponse({'status':'success','updated_table_html':updated_table_html})
        
        except Guide.DoesNotExist:
            return JsonResponse({'status':'error','message':'item not found'})
        

        
def delete_guide_forever_view(request,pk):
    if request.method == 'POST' :
        try:
            data=Guide.objects.get(pk=pk)
            data.delete()
            all_data=Guide.objects.filter(is_deleted=True)
            updated_table_html=render_to_string('partials/guide_trash_table.html',{'data':all_data})
            return JsonResponse({'status':'success','updated_table_html':updated_table_html})
        
        except Driver.DoesNotExist:
            return JsonResponse({'status':'error','message':'item not found'})
        
        
        
        
        
def addreminder_view(request):
    try:
        if request.method == 'POST':
            form = Reminder_form(request.POST)
            if form.is_valid():
                form.save()
                reminder = Reminder.objects.all().values('reminder_id', 'name','description','date','time')
                reminder_list = list(reminder)
                return JsonResponse({'success': True, 'reminder': reminder_list})
            else:
                return JsonResponse({'success': False, 'errors': form.errors})
        else:
            form = Reminder_form()
            reminder = Reminder.objects.all()
        return render(request, 'addreminder.html', {'form': form, 'data': reminder})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)
    
    
    
    
    
def view_reminder(request):
    data=Reminder.objects.all()
    expired=data.filter(date__lt=timezone.now()).exclude(status='Expired')
    expired.update(status="Expired")
    
    return render(request,'viewreminder.html',{'data':data,'form':Reminder_filter_form})


def filter_reminder(request):
    form = Reminder_filter_form(request.GET)  # Initialize the form with GET data
    reminder = Reminder.objects.all()


    if form.is_valid():
        date_from = form.cleaned_data.get('date_from')
        date_to = form.cleaned_data.get('date_to')
        status = form.cleaned_data.get('status')
        

        if date_from:
            reminder = reminder.filter(date__gte=date_from)
        if date_to:
            reminder = reminder.filter(date__lte=date_to)
        if status and status != '______':
            reminder = reminder.filter(status=status)
       

    # Render the updated table as a partial HTML
    bookings_html = render_to_string('partials/reminder_table.html', {'data': reminder})

    # Return the HTML as a response
    return JsonResponse({'status': 'success', 'bookings_html': bookings_html})




def edit_reminder_view(request,pk):
    try:
        # Fetch the supplier instance to update
        reminder = Reminder.objects.get(pk=pk)
    except reminder.DoesNotExist:
        messages.error(request, 'reminder does not exist.')
        return redirect('viewreminder')  # Ensure 'supplier_list' is the correct URL name

    if request.method == 'POST':
        form = Reminder_form(request.POST,instance=reminder)

        # Check if both the form and the formset are valid
        if form.is_valid():
            
            date_value=form.cleaned_data.get('date')
            today = timezone.now().date()
            
            if date_value > today:
                reminder.status='Active'
            else:
                reminder.status='Expired'
            # Save the supplier form
            form.save()

            # Provide success feedback
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                # Fetch all supplier allocation data and render the updated table
                all_data = Reminder.objects.all()  # or you can filter as needed
                updated_table_html = render_to_string('partials/reminder_table.html', {'data': all_data})
                
                return JsonResponse({'status': 'success', 'updated_table_html': updated_table_html})
            
            return redirect('viewreminder')  # Ensure 'supplier_list' is the correct URL name

        else:
            # Provide warning feedback if any form or formset is invalid
            messages.warning(request, 'Updating guide failed.')
            print(form.errors)
    
    else:
        # For GET request, populate the forms with existing data
        form = Reminder_form(instance=reminder)
        form_html = render_to_string('partials/editreminder.html', {'form': form,'csrf_token': get_token(request)})
        return JsonResponse({'form_html': form_html})
    
    
    
def delete_reminder_view(request,pk):
   
    if request.method == 'POST':
        try:
            data=Reminder.objects.get(pk=pk)
            data.delete()
            all_data=Reminder.objects.all()
            updated_table_html=render_to_string('partials/reminder_table.html',{'data':all_data})
            
            return JsonResponse({'status':'success','updated_table_html':updated_table_html})
        
        except Reminder.DoesNotExist:
            return JsonResponse({'status':'error','message':'item not found'})
        
        
        
def addstatus_view(request):
    try:
        if request.method=='POST':
            form=Status_form(request.POST)
            if form.is_valid():
                form.save()
                data=Status_type.objects.all().values('id', 'status')
                status_list=list(data)
                return JsonResponse({'success':True,'status':status_list})
            else:
                return JsonResponse({'successs':False,'errors':form.errors})
        else:
            form=Status_form()
            data=Status_type.objects.all()
            return render(request,'addstatus.html',{'form':form,'data':data})
    except Exception as e:
        return JsonResponse({'success':False,'error':str(e)},status=500)
    
    
def add_company_type_view(request):
    try:
        if request.method=='POST':
            form=Company_type_form(request.POST)
            if form.is_valid():
                form.save()
                data=Company_type.objects.all().values('id', 'type_name')
                type_list=list(data)
                return JsonResponse({'success':True,'type':type_list})
            else:
                return JsonResponse({'successs':False,'errors':form.errors})
        else:
            form=Company_type_form()
            data=Company_type.objects.all()
            return render(request,'addcompanytype.html',{'form':form,'data':data})
    except Exception as e:
        return JsonResponse({'success':False,'error':str(e)},status=500)
    
def get_category_fields(request):
    """
    View to return field visibility for a selected category.
    """
    category_id = request.GET.get('category_id')  # Get the category_id from the request

    if not category_id:
        return JsonResponse({"success": False, "error": "Category ID is required."})

    try:
        # Fetch the category object
        category = Category.objects.get(category_id=category_id)

        # Create a dictionary of field names and their boolean values
        fields = {
            "trip_date":category.date,
            "trip_time":category.time,
            "no_of_adult": category.no_of_adult,
            "no_of_child": category.no_of_child,
            "no_of_infant": category.no_of_infant,
            "rate_of_adult": category.rate_of_adult,
            "rate_of_child": category.rate_of_child,
            "rate_of_infant": category.rate_of_infant,
            "pickup_location": category.pickup_location,
            "drop_location": category.drop_location,
            "room_no": category.room_no,
            "remark": category.remark,
            "date": category.date,
            "time": category.time,
            "pickup_time": category.pickup_time,
            "transfer_type": category.transfer_type,
            "vehicle_type": category.vehicle_type,
            "vehicle_name": category.vehicle_name,
            "no_of_luggage": category.no_of_luggage,
            "flight_time": category.flight_time,
        }

        # Respond with the field data
        return JsonResponse({"success": True, "fields": fields})

    except Category.DoesNotExist:
        return JsonResponse({"success": False, "error": "Category not found."})
    
    

def get_package_rates(request):
    package_id = request.GET.get('package_id')  # Get the package ID from the query parameters
    package = Package.objects.filter(package_id=package_id).first()  # Fetch the package from the database

    if package:
        # Return the rates as JSON
        response_data = {
            'adult_rate': package.adult_rate,
            'child_rate': package.child_rate,
            'infant_rate': package.infant_rate,
        }
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Package not found'}, status=404)  

def addbooking_view(request):
    if request.method == 'POST':
        form = Booking_form(request.POST)
        formset = booking_trip_formset(request.POST)

        # Check if both the form and the formset are valid
        if form.is_valid() and formset.is_valid():
            # Save the supplier form
            booking = form.save(commit=False)
            booking.save()

            # Associate the formset with the supplier
            formset.instance = booking

            # Save the contact details in the formset
            formset.save()

            # Provide success feedback
            print(request.POST)
            return JsonResponse({'success':True})
        else:
            print(request.POST)
            print(formset.errors)
            return JsonResponse({'success':False,'errors':form.errors})
   
    else:
        # For GET request, create empty forms
        form = Booking_form()
        formset = booking_trip_formset()  # Use empty queryset to avoid initial extra forms

    return render(request, 'addbooking.html', {'form': form, 'formset': formset})
    
    

def view_bookings(request):
    data=Booking_Trip_details.objects.filter(is_deleted=False).order_by('-booking_trip_id')
    booking = Booking.objects.filter(bookingtripdetails__isnull=True)
    booking.delete()
    a=Booking.objects.all()
    b=len(a)
    print(b,"booking with zero trip deleted")
    return render(request,'viewbookings.html',{'data':data,'form':Booking_filter_form})


def filter_bookings(request):
    form = Booking_filter_form(request.GET)  # Initialize the form with GET data
    bookings = Booking_Trip_details.objects.filter(is_deleted=False)


    if form.is_valid():
        date_from = form.cleaned_data.get('date_from')
        date_to = form.cleaned_data.get('date_to')
        category = form.cleaned_data.get('category')
        package = form.cleaned_data.get('package')
        customer = form.cleaned_data.get('customer')
        payment_mode = form.cleaned_data.get('payment_mode')
        payment_status = form.cleaned_data.get('payment_status')
        status = form.cleaned_data.get('status')
        booked_by = form.cleaned_data.get('booked_by')
        supplier = form.cleaned_data.get('supplier')

        if date_from:
            bookings = bookings.filter(trip_date__gte=date_from)
        if date_to:
            bookings = bookings.filter(trip_date__lte=date_to)
        if category:
            bookings = bookings.filter(category__category_name__icontains=category)
        if package:
            bookings = bookings.filter(package__package_title__icontains=package)
            print(bookings.exists())
        if customer:
            print("customer")
            bookings = bookings.filter(booking__company_id=customer)
            
        if payment_mode:
            bookings = bookings.filter(booking__payment_mode_id=payment_mode)
        if payment_status and payment_status != '______':
            bookings = bookings.filter(booking__payment_status=payment_status)
        if status:
            bookings = bookings.filter(booking__status=status)
        if supplier:
            bookings = bookings.filter(supplier=supplier)

    # Render the updated table as a partial HTML
    bookings_html = render_to_string('partials/bookingtable.html', {'data': bookings})

    # Return the HTML as a response
    return JsonResponse({'status': 'success', 'bookings_html': bookings_html})




def edit_booking_view(request, pk):
    try:
        # Fetch the supplier instance to update
        booking = Booking.objects.get(pk=pk)
        trip_id=request.GET.get('trip_id')
    except Booking.DoesNotExist:
        messages.error(request, 'Booking does not exist.')
        return redirect('view_booking')  # Ensure 'supplier_list' is the correct URL name

    if request.method == 'POST':
        form = Booking_form(request.POST,instance=booking)
        formset = edit_booking_trip_formset(request.POST,instance=booking)

        # Check if both the form and the formset are valid and formset.is_valid()
        if form.is_valid() :
            # Save the supplier form
            booking = form.save(commit=False)
            booking.save()

            # Associate the formset with the supplier
            formset.instance = booking

            # # Save the contact details in the formset
            formset.save()

            # Provide success feedback
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                # Fetch all supplier allocation data and render the updated table
                all_data = Booking_Trip_details.objects.filter(is_deleted=False).order_by('-booking_trip_id')  # or you can filter as needed
                updated_table_html = render_to_string('partials/bookingtable.html', {'data': all_data})
                
                return JsonResponse({'status': 'success', 'updated_table_html': updated_table_html})
            
            return redirect('view_booking')  # Ensure 'supplier_list' is the correct URL name

        else:
            # Provide warning feedback if any form or formset is invalid
            messages.warning(request, 'Updating Booking failed.')
            print(form.errors)
            print(formset.errors)
            
    
    else:
        # For GET request, populate the forms with existing data
        form = Booking_form(instance=booking)
        formset = edit_booking_trip_formset(instance=booking,queryset=Booking_Trip_details.objects.filter(booking_trip_id=trip_id))
        trip_details=Booking_Trip_details.objects.filter(booking_trip_id=trip_id)
        
        for i in trip_details:
            i.total_adult_cost = i.no_of_adult * i.rate_of_adult
            i.total_child_cost = i.no_of_child * i.rate_of_child
            i.total_infant_cost = i.no_of_infant * i.rate_of_infant
            i.total_amount_=i.grand_total-i.vat_amount
            
        form_html = render_to_string('partials/editbooking.html', {'form': form,'formset':formset, 'csrf_token': get_token(request),'data':trip_details})
        return JsonResponse({'form_html': form_html})


   
def add_supplier_type_view(request):
    try:
        if request.method=='POST':
            form=Supplier_type_form(request.POST)
            if form.is_valid():
                form.save()
                data=Supplier_type.objects.all().values('id', 'type_name')
                type_list=list(data)
                return JsonResponse({'success':True,'type':type_list})
            else:
                return JsonResponse({'successs':False,'errors':form.errors})
        else:
            form=Supplier_type_form()
            data=Supplier_type.objects.all()
            return render(request,'addsuppliertype.html',{'form':form,'data':data})
    except Exception as e:
        return JsonResponse({'success':False,'error':str(e)},status=500) 
    
    
def booking_details_view(request,pk):
    data=Booking_Trip_details.objects.get(pk=pk)
    company=data.booking.company
    return render(request,'bookingdetailsview.html',{'data':data,'company':company})


def delete_bookings_view(request,pk):
    if request.method == 'POST' :
        try:
            data=Booking_Trip_details.objects.get(pk=pk)
            data.is_deleted = True
            data.save()
            
            all_data=Booking_Trip_details.objects.filter(is_deleted=False).order_by('-booking_trip_id')
            updated_table_html=render_to_string('partials/bookingtable.html',{'data':all_data})
            return JsonResponse({'status':'success','updated_table_html':updated_table_html})
        
        except Booking.DoesNotExist:
            return JsonResponse({'status':'error','message':'item not found'})
        
        
def recover_booking_view(request,pk):
    if request.method == 'POST' :
        try:
            data=Booking_Trip_details.objects.get(pk=pk)
            data.is_deleted = False
            data.save()
            
            all_data=Booking_Trip_details.objects.filter(is_deleted=True).order_by('-booking_trip_id')
            updated_table_html=render_to_string('partials/booking_trash_table.html',{'data':all_data})
            return JsonResponse({'status':'success','updated_table_html':updated_table_html})
        
        except Booking_Trip_details.DoesNotExist:
            return JsonResponse({'status':'error','message':'item not found'})
        
        
def recover_multiple_bookings(request):
    if request.method == 'POST':
        try:
            print(request.body)
            # Get the list of booking_trip_ids from the request
            data = json.loads(request.body)
            booking_trip_ids = data.get('booking_trip_ids', [])

            if booking_trip_ids:
                # Update 'is_deleted' to False for all selected booking_trip_ids
                Booking_Trip_details.objects.filter(booking_trip_id__in=booking_trip_ids).update(is_deleted=False)

                # Fetch the updated table HTML
                updated_table_html = render_to_string('partials/booking_trash_table.html', {
                    'data': Booking_Trip_details.objects.filter(is_deleted=True).order_by('-booking_trip_id'),  # Modify this to get the updated list of bookings
                })

                return JsonResponse({
                    'status': 'success',
                    'updated_table_html': updated_table_html,
                })
            else:
                return JsonResponse({'status': 'error', 'message': 'No IDs provided.'})

        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})



def delete_multiple_bookings_forever(request):
    if request.method == 'POST':
        try:
            print(request.body)
            # Get the list of booking_trip_ids from the request
            data = json.loads(request.body)
            booking_trip_ids = data.get('booking_trip_ids', [])

            if booking_trip_ids:
                # Update 'is_deleted' to False for all selected booking_trip_ids
                Booking_Trip_details.objects.filter(booking_trip_id__in=booking_trip_ids).delete()

                # Fetch the updated table HTML
                updated_table_html = render_to_string('partials/booking_trash_table.html', {
                    'data': Booking_Trip_details.objects.filter(is_deleted=True).order_by('-booking_trip_id'),  # Modify this to get the updated list of bookings
                })

                return JsonResponse({
                    'status': 'success',
                    'updated_table_html': updated_table_html,
                })
            else:
                return JsonResponse({'status': 'error', 'message': 'No IDs provided.'})

        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})




def delete_multiple_bookings(request):
    if request.method == 'POST':
        try:
            print(request.body)
            # Get the list of booking_trip_ids from the request
            data = json.loads(request.body)
            booking_trip_ids = data.get('booking_trip_ids', [])

            if booking_trip_ids:
                # Update 'is_deleted' to False for all selected booking_trip_ids
                Booking_Trip_details.objects.filter(booking_trip_id__in=booking_trip_ids).update(is_deleted=True)

                # Fetch the updated table HTML
                updated_table_html = render_to_string('partials/bookingtable.html', {
                    'data': Booking_Trip_details.objects.filter(is_deleted=False).order_by('-booking_trip_id'),  # Modify this to get the updated list of bookings
                })

                return JsonResponse({
                    'status': 'success',
                    'updated_table_html': updated_table_html,
                })
            else:
                return JsonResponse({'status': 'error', 'message': 'No IDs provided.'})

        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})
        
        
def delete_booking_forever_view(request,pk):
    if request.method == 'POST' :
        try:
            data=Booking_Trip_details.objects.get(pk=pk)
            data.delete()
            all_data=Booking_Trip_details.objects.filter(is_deleted=True).order_by('-booking_trip_id')
            updated_table_html=render_to_string('partials/booking_trash_table.html',{'data':all_data})
            return JsonResponse({'status':'success','updated_table_html':updated_table_html})
        
        except Booking_Trip_details.DoesNotExist:
            return JsonResponse({'status':'error','message':'item not found'})
        
    
     
def view_booking_trash(request):
    data=Booking_Trip_details.objects.filter(is_deleted=True).order_by('-booking_trip_id')
    return render(request,'bookingstrash.html',{'data':data})




def get_locations(request):
    search_query = request.GET.get('search', '')
    locations = Place.objects.filter(place_name__icontains=search_query)
    location_data = [{"name": location.place_name} for location in locations]
    
    print(location_data)  # Add this to inspect the response data
    
    return JsonResponse(location_data, safe=False)





def save_location(request):
    location_name = request.GET.get('location_name', '').strip()
    
    if location_name:
        # Check if the location exists
        location, created = Place.objects.get_or_create(place_name=location_name)
        
        if created:
            return JsonResponse({"success": True, "message": "Location saved."})
        else:
            return JsonResponse({"success": True, "message": "Location already exists."})
    
    return JsonResponse({"success": False, "message": "No location name provided."})



def get_company_details(request,company_id):
    try:
        company=Company.objects.get(pk=company_id)
        company_data={
            'id':company.company_id,
            'type':company.company_type.type_name,
            'status':company.status.status,
            'name':company.name,
            'address1':company.address1,
            'city1':company.city1,
            'state1':company.state1,
            'pincode1':company.pincode1,
            'country1':company.country1,
            'address2':company.address2,
            'city2':company.city2,
            'state2':company.state2,
            'pincode2':company.pincode2,
            'country2':company.country2,
            'email': company.email,
            'phone': company.mobile,
            'vat_no': company.vat_number,
            'tl_no': company.tl_number,
        }
        return JsonResponse({'success':True,'company':company_data})
    except Company.DoesNotExist:
        return JsonResponse({'success':False,'message':'Company not Found'},status=404)
    
    

def get_package_details(request, package_id):
    try:
        # Fetch the package object
        package = Package.objects.get(pk=package_id)

        try:
            # Try to get the supplier allocation for the package
            supplier_allocation = Supplier_allocation.objects.filter(package=package)
            
            # Debugging: Check the supplier_allocation object
            print(f"Supplier allocation found for package {package.package_id}: {supplier_allocation}")
            
            suppliers = []
            
            for allocation in supplier_allocation :
                if allocation.supplier:
                    # If supplier is a ForeignKey (one-to-one relationship)
                    suppliers.append(allocation.supplier)
                else:
                    # If supplier is a ManyToManyField (many-to-many relationship)
                    suppliers.extend(allocation.supplier.all())

            # Debugging: Check if suppliers are being fetched
            if suppliers:
                print(f"Found {len(suppliers)} suppliers for package {package.package_id}")
            else:
                print(f"No suppliers found for package {package.package_id}")

            # Prepare the supplier data
            supplier_data = []
            for supplier in suppliers:
                supplier_data.append({
                    'supplier_id': supplier.supplier_id,
                    'supplier_name': supplier.name,
                    'supplier_category': supplier.category.category_name,
                    'supplier_type': supplier.supplier_type.type_name,
                    'status': supplier.status.status,
                    'adult_price':allocation.adultprice,
                    'child_price':allocation.childprice,
                    'infant_price':allocation.infantprice,


                    
                })
        except Supplier_allocation.DoesNotExist:
            # Logging when no supplier allocation is found
            print(f"No supplier allocation found for package {package.package_id}")
            supplier_data = []

        # Prepare the package data
        package_data = {
            'id': package.package_id,
            'title': package.package_title,
            'category': package.package_category.category_name,
            'city': package.package_city,
            'status': package.status.status,
            'adult_price': package.adult_rate,
            'child_price': package.child_rate,
            'infant_price': package.infant_rate,
            'adult_age': package.adult_age,
            'child_age': package.child_age,
            'infant_age': package.infant_age,
            'description': package.description,
            'highlights': package.highlights,
            'inclusions': package.inclusions,
            'exclusions': package.exclusions,
            'open_hours': package.open_hours,
            'sunday': package.sunday,
            'monday': package.monday,
            'tuesday': package.tuesday,
            'wednesday': package.wednesday,
            'thursday': package.thursday,
            'friday': package.friday,
            'saturday': package.saturday,
            'supplier': supplier_data,
        }

        # Return the package data as JSON response
        return JsonResponse({'success': True, 'package': package_data})

    except Package.DoesNotExist:
        # Return error response if the package is not found
        return JsonResponse({'success': False, 'message': 'Package not found'}, status=404)

    except Exception as e:
        # Catch other errors and return a generic error response
        return JsonResponse({'success': False, 'message': str(e)}, status=500)

    
    
def delete_multiple_driver(request):
    if request.method == 'POST':
        try:
            print(request.body)
            # Get the list of booking_trip_ids from the request
            data = json.loads(request.body)
            driver_ids = data.get('driver_ids', [])

            if driver_ids:
                # Update 'is_deleted' to False for all selected booking_trip_ids
                Driver.objects.filter(driver_id__in=driver_ids).update(is_deleted=True)

                # Fetch the updated table HTML
                updated_table_html = render_to_string('partials/driver_table.html', {
                    'data': Driver.objects.filter(is_deleted=False),  # Modify this to get the updated list of bookings
                })

                return JsonResponse({
                    'status': 'success',
                    'updated_table_html': updated_table_html,
                })
            else:
                return JsonResponse({'status': 'error', 'message': 'No IDs provided.'})

        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})