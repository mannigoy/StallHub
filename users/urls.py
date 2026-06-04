from django.urls import path
from . import views

app_name = 'users'


urlpatterns = [
    path('login/',        views.login_view,       name='login'),
    path('register/',     views.register_view,    name='register'),
    path('dashboard/',    views.dashboard_view,   name='dashboard'),
    path('edit-profile/', views.edit_profile_view, name='edit_profile'),
    path('add-record/',   views.add_record_view,  name='add_record'),
    path('logoff/',       views.logoff_view,      name='logoff'),
]