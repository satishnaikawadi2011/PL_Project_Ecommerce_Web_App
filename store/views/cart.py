from django.shortcuts import render,redirect
from ..models.product import Product
from django.views import View



class Cart(View):
    def get(self,request):
        # print(request.session.get('cart'))
        if(request.session.get('cart')):
                ids = list(request.session.get('cart').keys())
                products = Product.get_products_by_ids(ids)
        else:
            products = False
        print(products)
        return render(request,'cart.html',{'products':products})