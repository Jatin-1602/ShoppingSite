from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category

# Create your views here.
def store(request, category_slug=None):
    category = None
    products = None

    if category_slug is not None:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, is_available=True)
    else:
        products = Product.objects.all().filter(is_available=True)

    product_count = products.count()

    context = {
        'products' : products,
        'product_count' : product_count,
    }

    return render(request, 'store/store.html', context)

def product_detail(request, category_slug=None, product_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    try:
        # Fetch single query
        product = Product.objects.get(category=category, slug=product_slug)
    except Exception as e:
        raise e

    # print(product.product_name)
    # print(product.price)

    context = {
        'product' : product,
    }

    return render(request, 'store/product_detail.html', context)