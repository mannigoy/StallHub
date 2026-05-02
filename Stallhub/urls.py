from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path("", lambda request: redirect("/vendors/login/")),    path("admin/", admin.site.urls),
    path("vendors/", include("vendors.urls")),
    path("users/", include("users.urls")),
    path("rentals/", include("rentals.urls")),
    path("stalls/", include("stalls.urls")),
    path("payments/", include("payments.urls")),
    path("maintenance/", include("maintenance.urls")),
]