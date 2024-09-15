from django.shortcuts import render
from catalog.models import Product

import catalog


# Create your views here.
# def index(request):
#     return render(request, 'catalog/base.html')

def products_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'catalog/base.html', context)

def contacts(request):
    return render(request, 'catalog/contacts.html')


