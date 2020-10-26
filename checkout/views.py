from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    shopping_bag = request.session.get('shopping_bag', {})
    if not shopping_bag:
        messages.error(request, "Thers nothing in your shopping bag!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    context = {
        'order_form': order_form
    }

    return render(request, 'checkout/checkout.html', context)
