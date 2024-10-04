from django.contrib import admin

from products.models import Product, LineOfBusiness, MetaField, ProductMetaFields, StringMetaField, NumberMetaField, DateMetaField

admin.site.register(Product)
admin.site.register(LineOfBusiness)
admin.site.register(MetaField)
admin.site.register(ProductMetaFields)
admin.site.register(StringMetaField)
admin.site.register(NumberMetaField)
admin.site.register(DateMetaField)