from django.contrib import admin
from django.urls import path, include
from rentals import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('rentals/', include('rentals.urls')),
    path('users/', include('users.urls')),
]