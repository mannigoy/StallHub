from django.contrib import admin
from stalls.models import Stall
from maintenance.models import MaintenanceRequest
from rentals.models import RentalHistory
from payments.models import Payment
from vendors.models import Vendor
from users.models import User

admin.site.register(Stall)
admin.site.register(MaintenanceRequest)
admin.site.register(RentalHistory)
admin.site.register(Payment)
admin.site.register(Vendor)
admin.site.register(User)


# Register your models here.
