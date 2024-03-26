from django.db import models
import uuid

from apps.establishment.models import Establishment


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
    name = models.CharField(max_length=100, verbose_name="Name")
    description = models.TextField(verbose_name="Description")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")
    quantity_in_stock = models.IntegerField(verbose_name="Quantity in Stock")
    unit = models.CharField(max_length=20)
    production_date = models.DateField()
    expiration_date = models.DateField()
    category = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    establishment = models.ForeignKey(Establishment, on_delete=models.CASCADE, related_name='products')

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name
    


