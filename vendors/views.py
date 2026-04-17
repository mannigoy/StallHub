from django.shortcuts import render, redirect
from .forms import VendorForm

def index(request):
    return render(request, 'index.html')

def add_new_vendor(request):
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = VendorForm()

    return render(request, 'addNewVendors.html', {'form': form})