from django.db import models
from vendors.models import Vendor
from stalls.models import Stall


class RentalAgreement(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('ended', 'Ended'),
    ]

    agreement_id = models.AutoField(primary_key=True)
    vendor = models.ForeignKey(
        Vendor, on_delete=models.CASCADE, related_name='agreements'
    )
    stall = models.ForeignKey(
        Stall, on_delete=models.CASCADE, related_name='agreements'
    )
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    rental_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return f"Agreement #{self.agreement_id} - {self.vendor.full_name}"


class RentalHistory(models.Model):
    history_id = models.AutoField(primary_key=True)
    agreement = models.ForeignKey(
        RentalAgreement, on_delete=models.CASCADE, related_name='history'
    )
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"History #{self.history_id} for Agreement #{self.agreement.agreement_id}"

    class Meta:
        verbose_name_plural = 'Rental Histories'


class Penalty(models.Model):
    penalty_id = models.AutoField(primary_key=True)
    agreement = models.ForeignKey(
        RentalAgreement, on_delete=models.CASCADE, related_name='penalties'
    )
    reason = models.TextField()
    penalty_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_issued = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Penalty #{self.penalty_id} - {self.reason[:40]}"

    class Meta:
        verbose_name_plural = 'Penalties'