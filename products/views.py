from django.shortcuts import render, get_object_or_404
from .models import Product
# Create your views here.


def all_products(request):
    """A view to return the products page with search queries"""

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_info(request, product_id):
    """ A view to render the product information """

    products = get_object_or_404(Product, pk=product_id)

    context = {
        'product': products,
    }

    return render(request, 'products/product_info.html', context)

