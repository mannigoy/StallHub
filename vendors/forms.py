from django import forms
from .models import Vendor

class VendorForm(forms.ModelForm):

    registration_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M']
    )

    class Meta:
        model = Vendor
        fields = ['user', 'full_name', 'contact_number', 'address', 'registration_date']