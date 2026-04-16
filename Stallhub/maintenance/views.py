from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import MaintenanceRequestForm

def index(request):
    return render(request, 'maintenance/index.html')


def add_new_maintenance_request(request):
    if request.method == 'POST':
        form = MaintenanceRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Maintenance request submitted successfully.')
            return redirect('maintenance:add_new_maintenance_request')
    else:
        form = MaintenanceRequestForm()

    # Get all maintenance requests, newest first
    from .models import MaintenanceRequest
    all_requests = MaintenanceRequest.objects.select_related('stall', 'requested_by').order_by('-request_date', '-request_id')

    return render(
        request,
        'maintenance/add_new_maintenance_request.html',
        {'form': form, 'all_requests': all_requests},
    )
