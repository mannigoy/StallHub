from django.urls import path
from . import views

app_name = 'stalls'

urlpatterns = [
    path('', views.login_view, name='login'),
    path('HomePage/', views.add_stall, name='add'),
    path('index/', views.index, name='index'),
    path('logout/', views.logout_view, name='logout'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),

]