from django.contrib import admin
from django.urls import path, include
from rentals import views

urlpatterns = [
    path('', views.index),  # "/" → index.html
    path('admin/', admin.site.urls),
    path('stalls/', include('stalls.urls')),
    path('vendors/', include('vendors.urls')),
    path('payments/', include('payments.urls')),
    path('rentals/', include('rentals.urls')),
    path('maintenance/', include('maintenance.urls')),
    path('users/', include('users.urls')),
]