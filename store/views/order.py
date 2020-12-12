from django.shortcuts import render,redirect
from ..models.product import Product
from django.views import View
from ..models.order import Order 
from ..models.customer import Customer



class OrderView(View):
    def get(self,request):
        customer = request.session.get('customer_id')
        orders = Order.get_orders_by_customer(customer)
        return render(request,'orders.html',{'orders':orders.reverse()})

