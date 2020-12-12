from django.shortcuts import render,redirect
from ..models.product import Product
from django.views import View
from ..models.order import Order 
from ..models.customer import Customer



class Checkout(View):
    def post(self,request):
        if not request.session.get('customer_id'):
            return redirect('login')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer_id')
        cart = request.session.get('cart')
        products = Product.get_products_by_ids(list(cart.keys()))
        # print(address,phone, customer)
        for product in products:
            order = Order(customer=Customer(id=customer),product=product,price=product.price,address=address,phone=phone,quantity=cart.get(str(product.id)))
            order.placeOrder()
        request.session['cart'] = {}
        return redirect('cart')

