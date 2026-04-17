from django import forms
from .models import Stall

class StallForm(forms.ModelForm):
    class Meta:
        model = Stall
        fields = '__all__'