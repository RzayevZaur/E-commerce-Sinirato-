from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import corep
from product.models import shoppagemodel,FeaturedProduct
from.forms import *


# Create your views here.


def index(request):
    
    products = shoppagemodel.objects.all()
    featured_Product=FeaturedProduct.objects.all()

    context = {

        'title': 'index page',
        'products': products,
        'featured_Product':featured_Product
      
  
       
    }
    return render(request, 'index.html', context=context)











def about(request):
    allabout = corep.objects.all()
    context = {

        'title': 'about page',
        "all": allabout

    }

    return render(request, 'about.html', context=context)


def wishlist(request):
    allwishlist = corep.objects.all()

    context = {

        'title': 'wishlist page',
        'all': allwishlist

    }

    return render(request, 'wishlist.html', context=context)







def contact(request):
    allcontact = corep.objects.all()
    if request.method == 'POST':
       form = contactforms(request.POST)
       if form.is_valid():
           form.save()
           return redirect('contact')
    else:
        form = contactforms()

    context = {

        'title': 'contact page',
        'all': allcontact, 
        'form': form

    }

    return render(request, 'contact-us.html', context=context)
