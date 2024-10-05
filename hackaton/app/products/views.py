from django.urls import reverse

from django.shortcuts import render, HttpResponseRedirect

from products.forms import ProductForm
from products.models import Product, LineOfBusiness

def index(request):
    return render(request, 'products/index.html')

def products(request):
    context = {
        'products': Product.objects.all(),
        'LOBID' : LineOfBusiness.objects.all(),
    }
    return render(request, 'products/products.html', context)


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('products:create_product'))
        else:
            print(form.errors)
    else:
        form = ProductForm()
    context = {'form': form}
    return render(request, 'products/create_product.html', context)