from django.db import models
from django.utils import timezone
# Ensure you have access to Product and Account models by importing them
# Assuming they are in 'inventory.models' and 'accounts.models' respectively.
# Adjust the import paths if your app structure is different.
from inventory.models import Product
from accounts.models import Account

class Invoice(models.Model):
    INVOICE_TYPE_CHOICES = [
        ('sales', 'Sales'),
        ('purchase', 'Purchase'),
    ]

    invoice_number = models.CharField(max_length=50, unique=True)
    date = models.DateField(default=timezone.now)
    account = models.ForeignKey(Account, on_delete=models.PROTECT) # Protect deletion of account if invoices are linked
    invoice_type = models.CharField(max_length=10, choices=INVOICE_TYPE_CHOICES)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00) # Will be calculated from items

    def __str__(self):
        return f"Invoice {self.invoice_number} - {self.account.name}"

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT) # Protect product deletion if part of an invoice
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2) # Can be pre-filled from Product, but overridable
    subtotal = models.DecimalField(max_digits=12, decimal_places=2) # Calculated as quantity * unit_price

    def save(self, *args, **kwargs):
        self.subtotal = self.quantity * self.unit_price
        super().save(*args, **kwargs)
        # Update the total_amount on the related Invoice instance
        self.invoice.total_amount = sum(item.subtotal for item in self.invoice.items.all())
        self.invoice.save()


    def __str__(self):
        return f"{self.quantity} x {self.product.name} on {self.invoice.invoice_number}"
