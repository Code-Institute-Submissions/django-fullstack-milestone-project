from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from .models import Bonus

import datetime


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })

    # In contexts.py when you calculate the grand total

    now = datetime.datetime.now().date()
    free_delivery_discount = Bonus.objects.filter(
        name="FREE_DELIVERY_THRESHOLD",
        expires_on__gte=now,
        is_active=True).first()

    if not free_delivery_discount:
        # Discount doesn't exist, calculate normally
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = None
    else:
        if total < free_delivery_discount.amount:
            # Discount exists, but user has to pay more to qualify
            delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
            free_delivery_delta = free_delivery_discount.amount - total
        else:
            # Discount exists, user is above threshold
            delivery = 0
            free_delivery_delta = 0

    grand_total = delivery + total

    free_delivery_discount_amount = free_delivery_discount.amount

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': free_delivery_discount_amount,
        'grand_total': grand_total,
    }

    return context
