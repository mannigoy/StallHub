from django import forms
from .models import Stall


class StallForm(forms.ModelForm):

    class Meta:
        model = Stall
        fields = [
            'stall_number',
            'location',
            'operating_hours',
            'monthly_rent',
            'market',
            'category',
        ]

        widgets = {
            'stall_number': forms.TextInput(attrs={
                'placeholder': 'Enter stall number'
            }),

            'monthly_rent': forms.NumberInput(attrs={
                'placeholder': 'Enter monthly rent'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Make dropdowns user-friendly
        self.fields['location'].empty_label = "Select Location"
        self.fields['operating_hours'].empty_label = "Select Operating Hours"
        self.fields['market'].empty_label = "Select Market"
        self.fields['category'].empty_label = "Select Category"
