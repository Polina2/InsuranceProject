from django.db import models

class LineOfBusiness(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=128)
    LOBID = models.ForeignKey(LineOfBusiness, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products_images', blank=True)
    name_for_str_metafield = models.CharField(max_length=128, null=True, blank=True)
    str_value = models.CharField(max_length=128, null=True, blank=True)
    name_for_numeric_metafield = models.CharField(max_length=128, null=True, blank=True)
    numeric_value = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    name_for_date_metafield = models.CharField(max_length=128, null=True, blank=True)
    begin = models.DateField(max_length=128, null=True, blank=True)
    end = models.DateField(max_length=128, null=True, blank=True)

    def __str__(self):
        return f'Продукт: {self.name} | Линия бизнеса: {self.LOBID.name}'

