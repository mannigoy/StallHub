from django import forms
from .models import RentalAgreement

class RentalAgreementForm(forms.ModelForm):
    class Meta:
        model = RentalAgreement
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        stall = cleaned_data.get('stall')

        if stall:
            existing = RentalAgreement.objects.filter(
                stall=stall,
                rental_status='active'
            )

            if existing.exists():
                raise forms.ValidationError("This stall is already rented.")

        return cleaned_data