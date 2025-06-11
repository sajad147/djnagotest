from django.db import models

class Warehouse(models.Model):
    name = models.CharField(max_length=255)
    location = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('product', 'warehouse') # Ensure no duplicate stock entries for the same product in the same warehouse

    def __str__(self):
        return f"{self.product.name} in {self.warehouse.name}: {self.quantity}"
