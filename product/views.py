from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import shoppagemodel,Category,Manufacturer,color
# Create your views here.


def details (request,pk):
    productdetail = get_object_or_404(shoppagemodel, pk=pk)
    detailspage=shoppagemodel.objects.all()

    context ={
       
       'title':'shoppage',
       'detailspage':detailspage,
       'productdetail':productdetail
    }
    return render(request,'product-details.html',context=context)















def shoppage(request):
    shops=shoppagemodel.objects.all()
    categories = Category.objects.all()
    manufacturer=Manufacturer.objects.all()
    colors=color.objects.all()

    context={
       
        'title':'crops',
        'shops':shops,
        'categories':categories,
        'manufacturer': manufacturer,
        'colors':colors
    }
    return render (request,'shop-grid-left-sidebar-4-column.html',context=context)





def shoppage_1(request, slug):
    shops = shoppagemodel.objects.filter(Category__slug=slug)
    categories = Category.objects.all()
    manufacturer=Manufacturer.objects.all()
    colors=color.objects.all()

        
    context={
        'title':'crops',
        'categories':categories,
        'shops': shops,
        'manufacturer': manufacturer,
        'colors':colors
    }
    return render (request,'shop-grid-left-sidebar-4-column.html',context=context)





def shoppage_2(request,slug):
    shops=shoppagemodel.objects.filter(Manufacturer__slug=slug)
    categories = Category.objects.all()
    manufacturer=Manufacturer.objects.all()
    colors=color.objects.all()

    context={
       
        'title':'crops',
        'shops':shops,
        'categories':categories,
        'manufacturer':manufacturer,
        'colors':colors

    }
    return render (request,'shop-grid-left-sidebar-4-column.html',context=context)




def shoppage_3(request,slug):
    shops=shoppagemodel.objects.filter(color__slug=slug)
    categories = Category.objects.all()
    manufacturer=Manufacturer.objects.all()
    colors=color.objects.all()

    context={
       
        'title':'crops',
        'shops':shops,
        'categories':categories,
        'manufacturer': manufacturer,
        'colors':colors
    }
    return render (request,'shop-grid-left-sidebar-4-column.html',context=context)








