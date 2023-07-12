from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse


# Create your views here.


def login(request):
    now=timezone.now()
    context={

        'vaxt':now,
        'title':'login page',

    }
    return render(request,'login.html',context=context)
     




def myaccount(request):
    now=timezone.now()
    context={

        'vaxt':now,
        'title':'my-account page',

    }
    return render(request,'my-account.html',context=context)
     
     

def register(request):
    now=timezone.now()
    context={

        'vaxt':now,
        'title':'register page',
    }
    return render(request,'register.html',context=context)
     
     

