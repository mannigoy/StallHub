from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RentalAgreementForm
from .models import RentalAgreement  # 👈 ADD THIS

@login_required(login_url='/users/login/')
def index(request):
    return render(request, 'index.html')

@login_required(login_url='/users/login/')
def add_record(request):
    if request.method == 'POST':
        form = RentalAgreementForm(request.POST)
        if form.is_valid():
            rental = form.save()

            # OPTIONAL: auto-set stall to occupied
            stall = rental.stall
            stall.status = 'occupied'
            stall.save()

            return redirect('/rentals/')
    else:
        form = RentalAgreementForm()

    return render(request, 'addNewRentalAgreement.html', {'form': form})


# 👇 NEW FUNCTION (VIEW RECORDS)
@login_required(login_url='/users/login/')
def view_records(request):
    records = RentalAgreement.objects.all()
    return render(request, 'viewRecords.html', {'records': records})