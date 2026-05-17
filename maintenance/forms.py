from django import forms

from .models import MaintenanceRequest


class MaintenanceRequestForm(forms.ModelForm):
    class Meta:
        model = MaintenanceRequest
        fields = ["stall", "requested_by", "issue_description", "status"]
        widgets = {
            "issue_description": forms.Textarea(attrs={"rows": 4}),
        }

