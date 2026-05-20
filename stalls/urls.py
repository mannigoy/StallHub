from django.urls import path
from . import views

app_name = 'stalls'

urlpatterns = [
    path('', views.index, name='index'),
    path('NewStall/', views.add_stall, name='add_stall')
]