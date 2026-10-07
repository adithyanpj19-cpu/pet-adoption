from django import template

register = template.Library()

@register.filter
def total_price(item):
    """Calculate total price of an item (price * quantity)."""
    return item.product.price * item.quantity
