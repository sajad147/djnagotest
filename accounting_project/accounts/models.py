from django.db import models

class Account(models.Model):
    ACCOUNT_TYPE_CHOICES = [
        ('customer', 'Customer'),
        ('vendor', 'Vendor'),
    ]

    name = models.CharField(max_length=255)
    contact_details = models.TextField(blank=True, null=True)
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPE_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.get_account_type_display()})"
