from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
# Create your views here.


def məhsul (request):
    now= timezone.now()
    context ={
       'məhsul': now,
       'title':'məhsullar'
   }
    return render(request,'product-details.html',context=context)




def crop(request):
    now= timezone.now()
    context={
        'crop':now,
        'title':'crops'
    }
    return render (request,'shop-grid-left-sidebar-4-column.html',context=context)