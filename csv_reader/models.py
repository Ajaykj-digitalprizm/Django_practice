from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class CSV_reader(models.Model):
    Product_Family = models.TextField(blank=True, null=True)
    Product_Code = models.TextField(blank=True, null=True, max_length=255)
    Product_Description = models.TextField(blank=True, null=True, max_length=255)
    Quantity_In_Stock = models.FloatField(validators=[MinValueValidator(0)])
    Available_Quantity = models.FloatField(validators=[MinValueValidator(0)])
    Allocated_Quantity = models.FloatField(validators=[MinValueValidator(0)])
    Price = models.FloatField(validators=[MinValueValidator(0)])
    Divider = models.FloatField(validators=[MinValueValidator(0)])

    def __str__(self):
        return self.Product_Code
