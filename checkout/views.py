from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    shopping_bag = request.session.get('shopping_bag', {})
    if not shopping_bag:
        messages.error(request, "There's nothing in your shopping bag!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HgttlKDmJHKEVPtuNisndH4iPd33sbFbgnKilVrQ4IosPQslrSug3bb2azAAVGTYfOd0EmagNyhxLOWm6Wb7qb900PhS0DeTx',
        'client_secret': 'test client secret',

    }

    return render(request, 'checkout/checkout.html', context)
