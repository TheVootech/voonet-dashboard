from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('',dashboard_view,name='dashboard'),
    path('addbooking',addbooking_view,name="add_booking"),
    path('viewbooking',viewbooking_view,name="view_booking"),
    
    path('viewdriverallocation',viewdriverallocation_view,name="view_driverallocation"),
    path('viewjobcard',view_jobcard_view,name="view_jobcard"),
    path('viewbookingreport',view_booking_report_view,name="view_booking_report"),
    path('viewjobreport',view_jobreport_view,name="view_job_report"),
    path('addpackage',addpackages_view,name="add_package"),
    
    path('addcategory',addcategory_view,name="add_category"),
    path('viewcategory',View_category,name="view_category"),
    path('editcategory/<str:pk>/',edit_category_view,name='editcategory'),
    path('deletecategory/<str:pk>/',delete_category_view,name='deletecategory'),



    
    path('addlanguage',addlanguage_view,name="add_language"),
    path('viewlanguage',View_language,name="viewlanguage"),
    path('editlanguage/<str:pk>/',edit_language_view,name='editlanguage'),
    path('deletelanguage/<str:pk>/',delete_language_view,name='deletelanguage'),


    
    path('addsupplier',addsupplier_view,name="add_supplier"),
    path('viewsupplier',Supplier_view,name="supplier"),
    path('editsupplier/<str:pk>/',update_supplier_view,name='editsupplier'),
    path('supplierdetailsview/<str:pk>/',supplier_details_view,name='supplier_details'),
    path('deletesupplier/<str:pk>/',delete_supplier_view,name='delete_supplier'),

    
    path('suppierallocation',Supplier_allocation_view,name='supplier_allocation'),
    path('allocatenewsupplier',Allocate_new_supplier_view,name='new_supplier_allocation'),
    path('editsupplierallocation/<int:pk>/',Edit_supplier_allocation_view,name='edit_supplier'),
    path('deletesupplierallocation/<int:pk>/',deletesupplierallocation_view,name='delete_supplier'),
    
    
    path('addcompany',addcompany_view,name="add_company"),
    path('viewcompany',view_company,name="company"),
    path('companydetailsview/<str:pk>/',company_detail_view,name='company_details'),
    path('editcompany/<str:pk>/',edit_company_view,name='editcompany'),
    path('deletecompany/<str:pk>/',delete_company_view,name='delete_company'),









    
   



    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)