from django.shortcuts import render, redirect

from django.http import HttpResponse



from .models import *
from.forms import *


# Create your views here.


def index(request):
    products = corep.objects.all()
    FeaturedProduct = corep.objects.all()
   

    context = {

        'title': 'index page',
        'products': products,
        'FeaturedProduct':FeaturedProduct
       
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
