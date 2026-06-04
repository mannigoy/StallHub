from django.db import models
from users.models import User


class Vendor(models.Model):
    vendor_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='vendor_profile', null=True, blank=True
    )
    full_name = models.CharField(max_length=200, unique=True)
    contact_number = models.CharField(max_length=20, unique=True)
    address = models.TextField()
    registration_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.full_name


class VendorDocument(models.Model):
    DOCUMENT_CHOICES = [
        ('vendor_application_form', 'Vendor Application / Stall Booking Form'),
        ('letter_of_intent', 'Letter of Intent'),
        ('stall_proposal_menu', 'Stall Proposal / Menu'),
        ('business_mayors_permit', "Business Permit / Mayor's Permit"),
        ('dti_sec_registration', 'DTI or SEC Registration'),
        ('bir_certificate', 'BIR Certificate of Registration (Form 2303)'),
        ('government_id', 'Government-Issued ID'),
        ('health_sanitation_permit', 'Health and Sanitation Permit'),
        ('food_business_license', 'Food Business License'),
        ('food_handlers_certificate', "Food Handler's Certificate"),
        ('medical_health_certificate', 'Medical / Health Certificate & Vaccination Card'),
        ('proof_of_payment', 'Proof of Payment'),
        ('certificate_of_insurance', 'Certificate of Insurance'),
        ('waiver_clearance', 'Waiver of Rights / Clearance'),
        ('other', 'Other'),
    ]

    document_id = models.AutoField(primary_key=True)
    vendor = models.ForeignKey(
        Vendor, on_delete=models.CASCADE, related_name='documents'
    )
    document_type = models.CharField(max_length=100, choices=DOCUMENT_CHOICES)
    expiry_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.document_type} - {self.vendor.full_name}"


class Violation(models.Model):
    violation_id = models.AutoField(primary_key=True)
    vendor = models.ForeignKey(
        Vendor, on_delete=models.CASCADE, related_name='violations'
    )
    inspection = models.ForeignKey(
        'maintenance.Inspection', on_delete=models.SET_NULL,
        null=True, blank=True, related_name='violations'
    )
    violation_type = models.CharField(max_length=100)
    penalty_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.violation_type} - {self.vendor.full_name}"