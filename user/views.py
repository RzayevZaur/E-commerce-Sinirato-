from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.


def login(request):

   

    context={

        'title':'login page',
   

    }
    return render(request,'login.html',context=context)
     




def myaccount(request):
 
    context={

        'title':'my-account page',

    }
    return render(request,'my-account.html',context=context)
     
     

def register(request):

    context={


        'title':'register page'
    }
    return render(request,'register.html',context=context)
     
     

