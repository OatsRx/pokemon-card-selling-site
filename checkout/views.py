from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from shoppingbag.contexts import shopping_bag_contents

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        shopping_bag = request.session.get('shopping_bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, quantity in shopping_bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity,
                    )
                    order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products you are trying to purchase wasn't found in our database. "
                        "Please Email @... for assisstance.")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('payment_success', args=[order.order_number]))
        else:
            messages.error(request, 'Your form was invalid. Please try again.')
    else:
        shopping_bag = request.session.get('shopping_bag', {})
        if not shopping_bag:
            messages.error(request, "There's nothing in your shopping bag!")
            return redirect(reverse('products'))

    current_bag = shopping_bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    order_form = OrderForm()
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,

    }

    return render(request, 'checkout/checkout.html', context)


def payment_success(request, order_number):
    """ Successful checkout payment """

    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Payment Success! :)')

    if 'shopping_bag' in request.session:
        del request.session['shopping_bag']

    context = {
        'order': order,
    }

    return render(request, 'checkout/payment_success.html', context)