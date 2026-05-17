from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')  # go to home
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


def profile_view(request):
    if not request.user.is_authenticated:
        return redirect('/users/login/')

    if request.method == 'POST':
        new_username = request.POST.get('username')

        if new_username:
            request.user.username = new_username
            request.user.save()
            return redirect('/users/profile/')

    return render(request, 'profile.html')


def logout_view(request):
    logout(request)
    return redirect('/users/login/')