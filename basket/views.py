from django.shortcuts import render
from .models import *
from .forms import *
from shop.models import Brawl



# Create your views here.
#view Корзины
def baskets(request):
    basket = Basket.objects.filter(user = request.user)
    all_price = 0
    for i in basket:
        all_price += i.brawl.price
    else:
        return render(request, 'basket.html', {'basket': basket,'all_price':all_price})

#view заказа
def order_items(request):
    basket = Basket.objects.filter(user = request.user)
    order_form = Order(request.POST)
    all_price = 0
    for i in basket:
        all_price += i.brawl.price
        i.brawl.order_count +=1
        i.brawl.save()
    if request.method == 'POST':
        if order_form.is_valid:
            preform = order_form.save(commit=False)
            preform.user = request.user
            preform.all_price = all_price
            preform.save()
            for item in basket:
                item.delete()
            return render(request,'finished.html')
    else:
        return render(request, 'order.html', {'form': order_form})
    
