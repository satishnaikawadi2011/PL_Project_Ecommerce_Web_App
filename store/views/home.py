from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.hashers import make_password,check_password
from ..models.product import Product
from ..models.category import Category
from .. models.customer import Customer
from django.views import View
from django.views.decorators.csrf import  csrf_exempt
# Create your views here.
# def index(request):
#     return HttpResponse('<h1>My Store App</h1>')

def index(request):
    products = None
    categories = Category.get_all_categories()
    categoryId = request.GET.get('category')
    if categoryId:
        products = Product.get_products_by_category(categoryId)
    else:
        products = Product.get_all_products();
    data = {}
    data['products'] = products
    data['categories'] = categories
    return render(request,'index.html',data)

     
@csrf_exempt
def add_to_cart(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        # print(request.session.session_key)
        isCart = check_cart(request)
        print(isCart)
        if isCart:
            cart = request.session['cart']
            quantity = cart.get(id)
            if quantity:
                cart[id] = quantity + 1
            else:
                cart[id] = 1
        else:
            cart = {}
            cart[id] = 1
        request.session['cart'] = cart
        print(f"Ypu are {request.session.get('email')}")
        print(cart)
        return JsonResponse({'quantity':"quantity"}) 

def increament_cart_quantity(request):
        if request.method == 'GET':
            id = request.GET.get('id')
            cart = request.session.get('cart')
            quantity = cart.get(id)
            cart[id] = quantity + 1
            request.session['cart'] = cart
            return JsonResponse({'quantity':quantity + 1}) 

def decreament_cart_quantity(request):
        if request.method == 'GET':
            id = request.GET.get('id')
            cart = request.session.get('cart')
            quantity = cart.get(id)
            if quantity == 1:
                cart.pop(id)
            else:
                cart[id] = quantity - 1
            request.session['cart'] = cart
            return JsonResponse({'quantity':quantity - 1})  

def check_cart(request):
        try:
            cart = request.session.get('cart')
            if not cart:
                return False
            else:
                return True
            # print("djdjnjkdejkde")
            # print(cart)
            # print('sbjbdjkdjkdjnk')
            return True
        except :
            return False



    
