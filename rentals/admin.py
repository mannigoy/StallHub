from django.contrib import admin
from .models import RentalAgreement, Penalty

admin.site.register(RentalAgreement)
admin.site.register(Penalty)