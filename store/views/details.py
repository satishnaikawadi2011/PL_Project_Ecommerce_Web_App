from django.shortcuts import render,redirect,HttpResponse
from ..models.product import Product
from django.views import View



class Detail(View):
    def get(self,request,pid):
        product = Product.objects.get(id=int(pid))
        # print(product.category)
        return render(request,'details.html',{'product':product})