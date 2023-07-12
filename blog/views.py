from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse

# Create your views here.


def blog(request):
    now=timezone.now()
    context= {
 
        'vaxt':now,
        'title':'blog page'

    }

    return render ( request,'blog-details.html',context=context)
    



def blogone (request):
    now=timezone.now()
    context= {
 
        'vaxt':now,
        'title':'blog page one'

    }

    return render ( request,'blog-right-sidebar-3.html',context=context)
    

