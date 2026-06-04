from django import forms
from .models import Stall
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


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

    def clean_stall_number(self):
        stall_number = self.cleaned_data.get('stall_number')

        existing_stall = Stall.objects.filter(stall_number=stall_number)

        if self.instance and self.instance.pk:
            existing_stall = existing_stall.exclude(pk=self.instance.pk)

        if existing_stall.exists():
            raise forms.ValidationError("This stall number already exists. Please enter a different stall number.")

        return stall_number

