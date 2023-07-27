from django.shortcuts import render
from store.models import Product

def index(request):
    products = Product.objects.all()
    context = {
        'products' : products,
    }

    return render(request, 'home.html', context)