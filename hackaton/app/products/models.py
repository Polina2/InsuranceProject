from django.db import models

class LineOfBusiness(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=128)
    LOBID = models.ForeignKey(LineOfBusiness, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products_images')

    def __str__(self):
        return f'Продукт: {self.name} | Линия бизнеса: {self.LOBID.name}'

class MetaField(models.Model):
    name = models.CharField(max_length=128, unique=True) # например, возраст

    def __str__(self):
        return self.name


class ProductMetaFields(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    metafield = models.ForeignKey(MetaField, on_delete=models.CASCADE)

    def __str__(self):
        return f'Продукт: {self.product.name} | Метаданные: {self.metafield.name}'

class NumberMetaField(models.Model):
    product_metadata = models.OneToOneField(ProductMetaFields, on_delete=models.CASCADE, primary_key=True)
    value = models.IntegerField()

    def __str__(self):
        return (f'Продукт {self.product_metadata.product.name} |'
                f'Метаданные: {self.product_metadata.metafield.name} |'
                f'Значение: {self.value}')


class DateMetaField(models.Model):
      product_metafield = models.OneToOneField(ProductMetaFields, on_delete=models.CASCADE, primary_key=True)
      begin = models.DateField()
      end = models.DateField()

      def __str__(self):
          return (f'Продукт {self.product_metafield.product.name} |'
                  f'Метаданные: {self.product_metafield.metafield.name} |'
                  f'Дата начала: {self.begin} | Дата конца {self.end}')

class StringMetaField(models.Model):
    product_metafield = models.OneToOneField(ProductMetaFields, on_delete=models.CASCADE, primary_key=True)
    value = models.CharField(max_length=128)
    def __str__(self):
        return (f'Продукт {self.product_metafield.product.name} |'
                f'Метаданные: {self.product_metafield.metafield.name} |'
                f'Значение: {self.value}')









