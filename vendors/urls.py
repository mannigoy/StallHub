from django.urls import path
from . import views

app_name = 'vendors'

urlpatterns = [
    path('', views.index,name='index'),
    path('addNewVendor/', views.add_new_vendor, name='addNewVendors')]