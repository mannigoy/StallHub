from django.urls import path
from . import views

app_name = 'vendors'

urlpatterns = [
    path('', views.index, name='index'),
    path('addNewVendor/', views.add_new_vendor, name='addNewVendors'),
    path('edit/<int:vendor_id>/', views.edit_vendor, name='edit_vendor'),
    path('delete/<int:vendor_id>/', views.delete_vendor, name='delete_vendor'),
]
