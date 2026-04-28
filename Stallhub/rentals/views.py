from django.shortcuts import render, redirect
from .forms import RentalAgreementForm

def index(request):
    return render(request, 'index.html')

def add_record(request):
    if request.method == 'POST':
        form = RentalAgreementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/rentals/')
    else:
        form = RentalAgreementForm()

    return render(request, 'addNewRentalAgreement.html', {'form': form})