from django.shortcuts import render


from products.models import Product, LineOfBusiness, MetaField, ProductMetaFields, StringMetaField, NumberMetaField, DateMetaField


def index(request):
    return render(request, 'products/index.html')

def products(request):
    context = {
        'products': Product.objects.all(),
        'LOBID' : LineOfBusiness.objects.all(),
        'metafields' : MetaField.objects.all(),
        'product_metafields' : ProductMetaFields.objects.all(),
        'string_fields' : StringMetaField.objects.all(),
        'number_fields' : NumberMetaField.objects.all(),
        'date_fields' : DateMetaField.objects.all(),
    }
    return render(request, 'products/products.html', context)