from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404

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


def edit_maintenance_request(request, request_id):
    from .models import MaintenanceRequest
    maintenance_request = get_object_or_404(MaintenanceRequest, request_id=request_id)

    if request.method == 'POST':
        form = MaintenanceRequestForm(request.POST, instance=maintenance_request)
        if form.is_valid():
            form.save()
            messages.success(request, 'Maintenance request updated successfully.')
            return redirect('maintenance:add_new_maintenance_request')
    else:
        form = MaintenanceRequestForm(instance=maintenance_request)

    return render(
        request,
        'maintenance/edit_maintenance_request.html',
        {'form': form, 'maintenance_request': maintenance_request},
    )


def delete_maintenance_request(request, request_id):
    from .models import MaintenanceRequest
    maintenance_request = get_object_or_404(MaintenanceRequest, request_id=request_id)

    if request.method == 'POST':
        maintenance_request.delete()
        messages.success(request, 'Maintenance request deleted successfully.')
        return redirect('maintenance:add_new_maintenance_request')

    return render(
        request,
        'maintenance/delete_maintenance_request.html',
        {'maintenance_request': maintenance_request},
    )
