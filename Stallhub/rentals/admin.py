from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import RentalAgreement, RentalHistory, Penalty

admin.site.register(RentalAgreement)
admin.site.register(RentalHistory)
admin.site.register(Penalty)