from django.db import models
from rentals.models import RentalAgreement


class PaymentMethod(models.Model):
    method_id = models.AutoField(primary_key=True)
    method_name = models.CharField(max_length=100)

    def __str__(self):
        return self.method_name


class Payment(models.Model):
    STATUS_CHOICES = [
        ('paid', 'Paid'),
        ('late', 'Late'),
    ]
    PERIOD_CHOICES = [
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly'),
    ]

    payment_id = models.AutoField(primary_key=True)
    agreement = models.ForeignKey(
        RentalAgreement, on_delete=models.CASCADE, related_name='payments'
    )
    payment_method = models.ForeignKey(
        PaymentMethod, on_delete=models.SET_NULL, null=True, blank=True
    )
    payment_date = models.DateField(auto_now_add=True)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='paid')
    payment_period = models.CharField(max_length=10, choices=PERIOD_CHOICES, default='monthly')
    period_month = models.PositiveSmallIntegerField(null=True, blank=True, help_text="Month number (1-12)")
    period_year = models.PositiveIntegerField(null=True, blank=True, help_text="e.g. 2025")

    def __str__(self):
        return f"Payment #{self.payment_id} - {self.payment_status}"