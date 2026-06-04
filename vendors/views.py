from django.shortcuts import render, redirect, get_object_or_404
from .forms import VendorForm, VendorDocumentForm
from .models import Vendor

def index(request):
    vendors = Vendor.objects.prefetch_related('documents').all()
    vendor_data = []
    for vendor in vendors:
        document = vendor.documents.order_by('document_id').first()
        vendor_data.append({'vendor': vendor, 'document': document})
    return render(request, 'vendors/index.html', {'vendor_data': vendor_data})

def add_new_vendor(request):
    if request.method == 'POST':
        form = VendorForm(request.POST)
        doc_form = VendorDocumentForm(request.POST)
        if form.is_valid() and doc_form.is_valid():
            vendor = form.save()
            document = doc_form.save(commit=False)
            document.vendor = vendor
            document.save()
            return redirect('vendors:index')
    else:
        form = VendorForm()
        doc_form = VendorDocumentForm()

    return render(
        request,
        'vendors/addNewVendors.html',
        {'form': form, 'doc_form': doc_form}
    )

def edit_vendor(request, vendor_id):
    vendor = get_object_or_404(Vendor, vendor_id=vendor_id)
    document = vendor.documents.order_by('document_id').first()

    if request.method == 'POST':
        form = VendorForm(request.POST, instance=vendor)
        doc_form = VendorDocumentForm(request.POST, instance=document)
        if form.is_valid() and doc_form.is_valid():
            vendor = form.save()
            document = doc_form.save(commit=False)
            document.vendor = vendor
            document.save()
            return redirect('vendors:index')
    else:
        form = VendorForm(instance=vendor)
        doc_form = VendorDocumentForm(instance=document)

    return render(
        request,
        'vendors/editVendor.html',
        {'form': form, 'doc_form': doc_form, 'vendor': vendor}
    )

def delete_vendor(request, vendor_id):
    vendor = get_object_or_404(Vendor, vendor_id=vendor_id)
    if request.method == 'POST':
        vendor.delete()
        return redirect('vendors:index')

    return render(request, 'vendors/deleteVendor.html', {'vendor': vendor})
