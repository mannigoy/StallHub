from django.contrib import admin

# Register your models here.

from .models import RentalAgreement, Penalty

admin.site.register(RentalAgreement)
admin.site.register(Penalty)