from django.shortcuts import render, redirect, get_object_or_404
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
        post_data = request.POST.copy()

        if 'monthly_rent' in post_data:
            post_data['monthly_rent'] = post_data['monthly_rent'].replace(',', '')

        form = StallForm(post_data)

        if form.is_valid():
            form.save()
            return redirect('stalls:add')
        else:
            print(form.errors)
    else:
        form = StallForm()

    return render(request, 'stalls/addNewStall.html', {
        'form': form,
        'user_name': request.user.first_name,
        'stalls': Stall.objects.all().order_by('-stall_id'),
    })


def index(request):
    if not request.user.is_authenticated:
        return redirect('stalls:login')

    stalls = Stall.objects.all()
    return render(request, 'stalls/index.html', {'stalls': stalls})


def logout_view(request):
    logout(request)
    return redirect('stalls:login')


def delete_stall(request, stall_id):
    if not request.user.is_authenticated:
        return redirect('stalls:login')

    stall = get_object_or_404(Stall, stall_id=stall_id)

    if request.method == 'POST':
        stall.delete()
        return redirect('stalls:add')

    return redirect('stalls:add')

def edit_stall(request, stall_id):
    if not request.user.is_authenticated:
        return redirect('stalls:login')

    stall = get_object_or_404(Stall, stall_id=stall_id)

    if request.method == 'POST':
        post_data = request.POST.copy()

        if 'monthly_rent' in post_data:
            post_data['monthly_rent'] = post_data['monthly_rent'].replace(',', '')

        form = StallForm(post_data, instance=stall)

        if form.is_valid():
            form.save()
            return redirect('stalls:add')
    else:
        form = StallForm(instance=stall)

    return render(request, 'stalls/addNewStall.html', {
        'form': form,
        'user_name': request.user.first_name,
        'stalls': Stall.objects.all().order_by('-stall_id'),
        'edit_mode': True,
        'stall': stall,
    })