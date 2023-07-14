from django.shortcuts import render, redirect
from django.db.models import Q
from .forms import DishForm, SaleForm
from django.contrib import messages
from django.http import HttpResponse
from .models import Dish, DishesType, Sale

toBuy = []

def home(request):
    
    return render(request, 'home.html')

def information(request):
    return render(request, 'information.html')

def typesofdishes(request):
    return render(request, 'typesofdishes.html')

def menu(request):
    if request.GET.get('q') != None:
        q = request.GET.get('q')
    else:
        q = ''

    dishes = Dish.objects.filter(
        Q(dishesType__name__icontains=q) |
        Q(title__icontains = q) 
    )
    
    types = DishesType.objects.all()
    context = {'dishes' : dishes, 'types' : types, 'q':q}
    return render(request, 'menu.html', context)

def dishinfo(request, pk):
    dish = Dish.objects.get(id=pk)
    context = {'dish':dish}
    return render(request, 'dishinfo.html', context)

#def cart(request):
#    cart_items = toBuy  # Retrieve cart items from the session
#    context = {'cart_items': cart_items}
#    return render(request, 'cart.html', context)

def sale(request):
    sales = Sale.objects.all()
    context = {'sales' : sales}
    return render(request, 'sale.html', context)
def saleinfo(request, pk):
    sale = Sale.objects.get(id=pk)
    if request.method == 'POST':
        toBuy.append(sale)
    context = {'sale':sale}
    return render(request, 'saleinfo.html', context)

