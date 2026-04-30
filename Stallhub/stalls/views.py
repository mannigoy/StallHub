from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import StallForm
from .models import Stall


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('stalls:add')
        else:
            return render(request, 'stalls/login.html', {'error': 'Invalid credentials'})

    return render(request, 'stalls/login.html')


def edit_profile(request):
    user = request.user

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        username = request.POST.get("username")

        user.username = username
        user.email = email
        user.first_name = name

        user.save()

        return redirect('stalls:edit_profile')

    return render(request, "stalls/edit_profile.html", {"user": user})


def add_stall(request):
    if not request.user.is_authenticated:
        return redirect('stalls:login')

    if request.method == 'POST':
        form = StallForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stalls:add')  # stay on same page
    else:
        form = StallForm()

    return render(request, 'stalls/addNewStall.html', {'form': form})


def index(request):
    if not request.user.is_authenticated:
        return redirect('stalls:login')

    stalls = Stall.objects.all()
    return render(request, 'stalls/index.html', {'stalls': stalls})


def logout_view(request):
    logout(request)
    return redirect('stalls:login')


