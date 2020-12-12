from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product,cart):
    keys = cart.keys()
    # print(product,cart)
    for id in keys:
        if int(id) == product.id:
            return True
    return False

@register.filter(name='cart_quantity')
def cart_quantity(product,cart):
    keys = cart.keys()
    # print(product,cart)
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0



@register.filter(name='product_price_subtotal')
def product_price_subtotal(product,cart):
    return product.price * cart_quantity(product,cart)

@register.filter(name='total_cart_price')
def total_cart_price(products,cart):
    sum = 0
    for p in products:
        sum += product_price_subtotal(p,cart)
    return sum

@register.filter(name='total_cart_items')
def total_cart_items(cart):
    total = 0
    for key in cart.keys():
        total += cart.get(key)
    return total

@register.filter(name="currency")
def currency(number):
    return "₹ " +str(number)

@register.filter(name="multiply")
def multiply(num1,num2):
    return num1 * num2