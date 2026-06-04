from django.urls import path
from . import views

app_name = 'maintenance'

urlpatterns = [
    path('', views.index, name='index'),
    path('newMaintenanceRequest', views.add_new_maintenance_request, name='add_new_maintenance_request'),
    path('edit/<int:request_id>/', views.edit_maintenance_request, name='edit_maintenance_request'),
    path('delete/<int:request_id>/', views.delete_maintenance_request, name='delete_maintenance_request'),
]