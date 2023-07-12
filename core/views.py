from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse

# Create your views here.


def index(request):
    now=timezone.now()
    context= {
 
        'vaxt':now,
        'title':'index page'

    }

    return render ( request,'index.html',context=context)





def about(request):
    now=timezone.now()
    context= {
 
        'vaxt':now,
        'title':'about page'

    }

    return render ( request,'about.html',context=context)




def wishlist(request):
    now=timezone.now()
    context= {
 
        'vaxt':now,
        'title':'wishlist page'

    }

    return render ( request,'wishlist.html',context=context)


