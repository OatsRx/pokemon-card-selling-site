from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_shopping_bag(request):
    """A view to render the shopping bag list"""

    return render(request, 'shoppingbag/shopping_bag.html')


def add_to_shopping_bag(request, item_id):
    """ Add items and their quantity to shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    shopping_bag = request.session.get('shopping_bag', {})

    if item_id in list(shopping_bag.keys()):
        shopping_bag[item_id] += quantity
    else:
        shopping_bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to shopping bag!')

    request.session['shopping_bag'] = shopping_bag
    return redirect(redirect_url)


def remove_from_shopping_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        shopping_bag = request.session.get('bag', {})

        if item_id in list(shopping_bag.keys()):
            shopping_bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from shopping bag!')

        request.session['shopping_bag'] = shopping_bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
