from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('addNewVendor/', views.add_new_vendor, name='add_vendor')]