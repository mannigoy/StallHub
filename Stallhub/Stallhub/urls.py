from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),          # ← changed
    path('stalls/', include('stalls.urls')),
    path('vendors/', include('vendors.urls')),
    path('payments/', include('payments.urls')),
    path('rentals/', include('rentals.urls')),
    path('maintenance/', include('maintenance.urls')),
    path('users/', include('users.urls')),
]