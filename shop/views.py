from django.shortcuts import render,reverse, get_object_or_404
from .models import *
from basket.models import Basket
from django.db.models import Q
# Create your views here.

#view основной страницы
def index(request,character_slug=None):
    character = None
    characters = Character.objects.all()
    brawls = Brawl.objects.filter(available=True)
    
    if character_slug:
        character = get_object_or_404(Character, slug=character_slug)
        brawls = brawls.filter(character=character)
        

    if request.method == "POST":
        brawl_slug = request.POST.get("add_basket")
        brawl = Brawl.objects.get(slug=brawl_slug)
        order = Basket.objects.create(user = request.user, brawl=brawl)
        
        
    return render(request,
                  'index.html',
                  {'company': character,
                   'companies': characters,
                   'products': brawls,})

#view страницы телефона
def brawl(request,brawl_slug):
   
    brawl = get_object_or_404(Brawl,slug=brawl_slug)
    
    brawl.views_count += 1
    brawl.save()
    
    if request.method == "POST":
        brawl_slug = request.POST.get("add_basket")
        brawl = Brawl.objects.get(slug=brawl_slug)
        order = Basket.objects.create(user = request.user, brawl=brawl)
    
    return render(request,"brawl.html",{'brawl':brawl})


#view поиска
def search(request):
    req = request.GET.get('searchbar')
    serach_result = Brawl.objects.filter(Q(name__icontains=req) | Q(slug__icontains=req) | Q(character__title__icontains=req))
    return render(request, 'search.html', {'results':serach_result,'req': req})
    
def contacts(request):
    return render(request, 'contacts.html')