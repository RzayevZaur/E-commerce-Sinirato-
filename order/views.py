from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
 
# Create your views here.


def order(request):
    now =timezone.now()
    context ={
            'vaxt': now,
            'title': 'order page'
    }
    
    return render (request,'cart.html',context=context)


def orders(request):
    now =timezone.now()


    context ={

        'vaxt': now,
        'title': 'orders html'
    }

    return render(request,'checkout.html',context=context)
    