from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('Username is required')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('role', 'admin')
        extra_fields.setdefault('account_status', 'active')
        return self.create_user(username, password, **extra_fields)


class User(AbstractBaseUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('vendor', 'Vendor'),
    ]
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('suspended', 'Suspended'),
    ]

    username = models.CharField(max_length=150, unique=True)
    account_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    date_created = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='vendor')
    last_login = models.DateTimeField(null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return f"{self.username} ({self.role})"


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='admin_profile')

    def __str__(self):
        return f"Admin: {self.user.username}"


class SystemAudit(models.Model):
    ACTION_CHOICES = [
        ('stall_update', 'Stall Update'),
        ('user_suspension', 'User Suspension'),
        ('rental_created', 'Rental Created'),
        ('payment_recorded', 'Payment Recorded'),
        ('violation_issued', 'Violation Issued'),
    ]

    log_id = models.AutoField(primary_key=True)
    action_type = models.CharField(max_length=50, choices=ACTION_CHOICES)
    affected_stall = models.ForeignKey(
        'stalls.Stall', on_delete=models.SET_NULL, null=True, blank=True
    )
    performed_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action_type} at {self.timestamp}"