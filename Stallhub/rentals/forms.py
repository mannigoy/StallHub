from django import forms
from .models import RentalAgreement

class RentalAgreementForm(forms.ModelForm):
    class Meta:
        model = RentalAgreement
        fields = '__all__'