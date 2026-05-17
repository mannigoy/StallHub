from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login_view),
    path('profile/', views.profile_view),
    path('logout/', views.logout_view),
]