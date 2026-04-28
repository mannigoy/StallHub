from django.urls import path
from . import views

app_name = 'rentals'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_record, name='add_record'),
]