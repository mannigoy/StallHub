from django.urls import path
from . import views

app_name = 'payments'


urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.add_payment, name='add_payment'),
    path('methods/new/', views.add_payment_method, name='add_payment_method'),
]