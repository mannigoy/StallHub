from django.urls import path
from . import views

app_name = 'maintenance'

urlpatterns = [
    path('', views.index, name='index'),
    path('newMaintenanceRequest', views.add_new_maintenance_request, name='add_new_maintenance_request'),
]