from django.shortcuts import render, redirect, get_object_or_404
from .forms import VendorForm, VendorDocumentForm
from .models import Vendor, VendorDocument
from rentals.models import RentalAgreement


def index(request):
    vendors = Vendor.objects.all()
    vendor_data = []

    for vendor in vendors:
        document = VendorDocument.objects.filter(vendor=vendor).first()
        vendor_data.append({
            'vendor': vendor,
            'document': document,
        })

    return render(request, 'vendors/index.html', {'vendor_data': vendor_data})


def add_vendor(request):
    if request.method == 'POST':
        vendor_form = VendorForm(request.POST)
        doc_form = VendorDocumentForm(request.POST)

        if vendor_form.is_valid() and doc_form.is_valid():
            vendor = vendor_form.save()
            document = doc_form.save(commit=False)
            document.vendor = vendor
            document.save()
            return redirect('vendors:index')
    else:
        vendor_form = VendorForm()
        doc_form = VendorDocumentForm()

    return render(request, 'vendors/addNewVendors.html', {
        'form': vendor_form,
        'doc_form': doc_form
    })


def edit_vendor(request, vendor_id):
    vendor = get_object_or_404(Vendor, pk=vendor_id)
    document = VendorDocument.objects.filter(vendor=vendor).first()

    if request.method == 'POST':
        vendor_form = VendorForm(request.POST, instance=vendor)
        doc_form = VendorDocumentForm(request.POST, instance=document)

        if vendor_form.is_valid() and doc_form.is_valid():
            vendor_form.save()
            doc = doc_form.save(commit=False)
            doc.vendor = vendor
            doc.save()
            return redirect('vendors:index')
    else:
        vendor_form = VendorForm(instance=vendor)
        doc_form = VendorDocumentForm(instance=document)

    return render(request, 'vendors/editVendor.html', {
        'form': vendor_form,
        'doc_form': doc_form,
        'current_document_type': document.document_type if document else '',
    })


def delete_vendor(request, vendor_id):
    vendor = get_object_or_404(Vendor, pk=vendor_id)

    if request.method == 'POST':
        vendor.delete()
        return redirect('vendors:index')

    return redirect('vendors:index')