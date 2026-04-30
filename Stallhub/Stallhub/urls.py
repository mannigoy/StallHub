from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('', views.index),  # "/" → index.html
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('maintenance/', include('maintenance.urls')),
    path('stalls/', include('stalls.urls')),
    path('vendors/', include('vendors.urls')),
    path('payments/', include('payments.urls')),
    path('rentals/', include('rentals.urls')),
    path('users/', include('users.urls')),
]