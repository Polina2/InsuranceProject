
from django.urls import path
from products.views import products, create_product

app_name = 'products'
urlpatterns = [
    path('', products, name='index'),
    path('create_product/', create_product, name='create_product'),
]

