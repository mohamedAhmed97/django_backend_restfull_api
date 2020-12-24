from django.db import models

# Create your models here.
class Product(models.Model):
    product_name=models.CharField(max_length=20)
    product_price=models.IntegerField()
    product_sales_start=models.DateField()
    product_sales_end=models.DateField()

    def __str__(self):
        return self.product_name
