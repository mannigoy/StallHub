from django import forms
from .models import Vendor, VendorDocument


class VendorForm(forms.ModelForm):
    registration_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M']
    )

    def clean_full_name(self):
        name = self.cleaned_data['full_name']
        qs = Vendor.objects.filter(full_name__iexact=name)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("A vendor with this name already exists.")
        return name

    def clean_contact_number(self):
        number = self.cleaned_data['contact_number']
        qs = Vendor.objects.filter(contact_number=number)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("This contact number is already registered.")
        return number

    class Meta:
        model = Vendor
        fields = ['user', 'full_name', 'contact_number', 'address', 'registration_date']


class VendorDocumentForm(forms.ModelForm):
    expiry_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False
    )

    class Meta:
        model = VendorDocument
        fields = ['document_type', 'expiry_date']