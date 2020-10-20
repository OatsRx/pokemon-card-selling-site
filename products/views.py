from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Product
# Create your views here.


def all_products(request):
    """A view to return the products page with search queries"""

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter seartch criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(rarity__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'products/products.html', context)


def product_info(request, product_id):
    """ A view to render the product information """

    products = get_object_or_404(Product, pk=product_id)

    context = {
        'product': products,
    }

    return render(request, 'products/product_info.html', context)

