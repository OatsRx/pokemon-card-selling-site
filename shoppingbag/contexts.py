from decimal import Decimal
from django.conf import settings


def shopping_bag_contents(request):
    """ A function to make context of shopping
    bag available across all templates """

    shopping_bag_items = []
    total = 0
    product_count = 0
    delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
    grand_total = delivery + total

    context = {
        'shopping_bag_items': shopping_bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total
    }

    return context
