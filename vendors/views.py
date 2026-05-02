from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import VendorForm

@login_required
def dashboard(request):
    return render(request, "vendors/dashboard.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("vendors:dashboard")
        else:
            messages.error(request, "Invalid credentials")

    return render(request, "vendors/login.html")


def logout_view(request):
    logout(request)
    return redirect("vendors:login")


@login_required
def profile(request):
    user = request.user

    if request.method == "POST":
        user.first_name = request.POST.get("first_name")
        user.email = request.POST.get("email")
        user.username = request.POST.get("username")
        user.save()

        messages.success(request, "Profile updated successfully")
        return redirect("vendors:profile")

    return render(request, "vendors/profile.html", {"user": user})


@login_required
def add_new_vendors(request):
    form = VendorForm()

    if request.method == "POST":
        form = VendorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("vendors:dashboard")

    return render(request, "vendors/addNewVendors.html", {"form": form})


@login_required
def delete_profile(request):
    if request.method == "POST":
        request.user.delete()
        return redirect("vendors:login")