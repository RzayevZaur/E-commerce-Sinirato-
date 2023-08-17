from django.shortcuts import render

from django.http import HttpResponse
 
# Create your views here.


def order(request):
   
    context ={
         
            'title': 'order page'
    }
    
    return render (request,'cart.html',context=context)


def orders(request):



    context ={

        
        'title': 'orders html'
    }

    return render(request,'checkout.html',context=context)
    