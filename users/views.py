from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .models import User


def login_view(request):
    if request.session.get('user_id'):
        return redirect('users:dashboard')

    error = None
    username = ''

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.account_status == 'suspended':
                error = 'Your account has been suspended. Please contact an administrator.'
            elif user.account_status == 'inactive':
                error = 'Your account is inactive. Please contact an administrator.'
            else:
                login(request, user)
                # Store basic info in session for easy template access
                request.session['user_id'] = user.pk
                request.session['username'] = user.username
                return redirect('users:dashboard')
        else:
            error = 'Invalid username or password. Please try again.'

    return render(request, 'users/login.html', {'error': error, 'username': username})


def register_view(request):
    if request.session.get('user_id'):
        return redirect('users:dashboard')

    errors = []
    form_data = {}

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        form_data = {'username': username}

        if not username:
            errors.append('Username is required.')
        elif len(username) < 3:
            errors.append('Username must be at least 3 characters.')
        elif User.objects.filter(username=username).exists():
            errors.append('That username is already taken.')

        if not password1:
            errors.append('Password is required.')
        elif len(password1) < 6:
            errors.append('Password must be at least 6 characters.')
        elif password1 != password2:
            errors.append('Passwords do not match.')

        if not errors:
            user = User.objects.create_user(username=username, password=password1)
            login(request, user)
            request.session['user_id'] = user.pk
            request.session['username'] = user.username
            return redirect('users:dashboard')

    return render(request, 'users/register.html', {'errors': errors, 'form_data': form_data})


def dashboard_view(request):
    if not request.session.get('user_id'):
        return redirect('users:login')
    return render(request, 'core/index.html')


def edit_profile_view(request):
    if not request.session.get('user_id'):
        return redirect('users:login')

    user = User.objects.get(pk=request.session['user_id'])
    success = None
    error = None

    if request.method == 'POST':
        new_username = request.POST.get('username', '').strip()
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')

        if not new_username:
            error = 'Username cannot be empty.'
        elif new_username != user.username and User.objects.filter(username=new_username).exists():
            error = 'That username is already taken.'
        elif password1 and password1 != password2:
            error = 'Passwords do not match.'
        elif password1 and len(password1) < 6:
            error = 'Password must be at least 6 characters.'
        else:
            user.username = new_username
            if password1:
                user.set_password(password1)
                update_session_auth_hash(request, user)
            user.save()
            request.session['username'] = user.username
            success = 'Profile updated successfully.'

    return render(request, 'users/edit_profile.html', {
        'user': user,
        'success': success,
        'error': error,
    })


def add_record_view(request):
    if not request.session.get('user_id'):
        return redirect('users:login')
    return render(request, 'users/add_record.html')


def logoff_view(request):
    logout(request)
    request.session.flush()
    return redirect('users:login')