from django.urls import path
from . import views

app_name = "vendors"

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("", views.dashboard, name="dashboard"),
    path("profile/", views.profile, name="profile"),
    path("addNewVendors/", views.add_new_vendors, name="addNewVendors"),
    path("delete/", views.delete_profile, name="delete_profile"),
]