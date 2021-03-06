from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order


def user_profile(request):
    """ A view to display the users profile """

    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=user_profile)
    orders = user_profile.orders.all()

    context = {
        'form': form,
        'orders': orders
    }
    return render(request, 'profiles/user_profile.html', context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past order for order number {order_number}'
    ))

    context = {
        'order': order,
        'from_profile': True
    }

    return render(request, 'checkout/payment_success.html', context)
