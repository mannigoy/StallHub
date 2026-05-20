from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [

    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', lambda request: redirect('users:dashboard')),
    path('maintenance/', include('maintenance.urls')),
    path('stalls/', include('stalls.urls')),
    path('vendors/', include('vendors.urls')),
    path('payments/', include('payments.urls')),
    path('rentals/', include('rentals.urls')),
    path('users/', include('users.urls')),
]