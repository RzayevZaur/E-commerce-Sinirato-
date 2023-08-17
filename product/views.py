from django.shortcuts import render
from django.http import HttpResponse
from .models import shoppagemodel,Category,Manufacturer
# Create your views here.


def details (request):
    detailspage=shoppagemodel.objects.all()

    context ={
       
       'title':'shoppage',
       'detailspage':detailspage
      
    }
    return render(request,'product-details.html',context=context)


def shoppage(request):
    categories = Category.objects.all()
    shop=shoppagemodel.objects.all()
    Manufacturers=Manufacturer.objects.all()


    context={
       
        'title':'crops',
        'shopcode':shop,
        'categories':categories,
        'manufacturers':Manufacturers

    }
    return render (request,'shop-grid-left-sidebar-4-column.html',context=context)


def shoppage_1(request, category):
    categories = Category.objects.all()
    products=shoppagemodel.objects.filter(Category__name=category).all()

    context={
        'shopcode':products,
        'categories':categories

    }
    return render (request,'shop-grid-left-sidebar-4-column.html',context=context)



def shoppage_2(request, manufacturer):

    brend=shoppagemodel.objects.filter(Manufacturer__name=manufacturer).all()
    Manufacturers=Manufacturer.objects.all()


    context={
       
        'title':'crops',
        'brends':brend,
        'manufacturers':Manufacturers

    }
    return render (request,'shop-grid-left-sidebar-4-column.html',context=context)


