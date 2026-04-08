from django.db import models


class Market(models.Model):
    market_id = models.AutoField(primary_key=True)
    market_name = models.CharField(max_length=200)
    location = models.CharField(max_length=255)
    operating_hours = models.CharField(max_length=100)

    def __str__(self):
        return self.market_name


class StallCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'Stall Categories'


class Stall(models.Model):
    STATUS_CHOICES = [
        ('occupied', 'Occupied'),
        ('vacant', 'Vacant'),
    ]

    stall_id = models.AutoField(primary_key=True)
    stall_number = models.CharField(max_length=20, unique=True)
    location = models.CharField(max_length=255)
    monthly_rent = models.DecimalField(max_digits=10, decimal_places=2)
    operating_hours = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='vacant')
    market = models.ForeignKey(
        Market, on_delete=models.SET_NULL, null=True, blank=True, related_name='stalls'
    )
    category = models.ForeignKey(
        StallCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='stalls'
    )

    def __str__(self):
        return f"Stall {self.stall_number} - {self.status}"