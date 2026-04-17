from django.shortcuts import render, redirect
from .forms import StallForm
from .models import Stall

def index(request):
    stalls = Stall.objects.all()
    return render(request, 'stalls/index.html')

def add_stall(request):
    if request.method == 'POST':
        form = StallForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stalls:index')
    else:
        form = StallForm()

    return render(request, 'stalls/addNewStall.html', {'form': form})