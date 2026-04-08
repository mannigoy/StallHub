from django.db import models
from stalls.models import Stall
from users.models import User


class MaintenanceRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('resolved', 'Resolved'),
    ]

    request_id = models.AutoField(primary_key=True)
    stall = models.ForeignKey(
        Stall, on_delete=models.CASCADE, related_name='maintenance_requests'
    )
    requested_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name='maintenance_requests'
    )
    issue_description = models.TextField()
    request_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Request #{self.request_id} - {self.status}"


class Inspection(models.Model):
    inspection_id = models.AutoField(primary_key=True)
    stall = models.ForeignKey(
        Stall, on_delete=models.CASCADE, related_name='inspections'
    )
    inspected_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name='inspections'
    )
    inspection_date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Inspection #{self.inspection_id} on {self.inspection_date}"