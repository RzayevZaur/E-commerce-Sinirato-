from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import (
    shoppagemodel,
    Category,
    Manufacturer,
    color,
    Review,
    Tags,
    Product_version,
    Category_color
)
from django.db.models import Count
from .forms import productform
from django.core.paginator import Paginator

# Create your views here.


def details(request, pk):
    productdetail = get_object_or_404(shoppagemodel, pk=pk)
    related_products = shoppagemodel.objects.filter(
        Category=productdetail.Category
    ).exclude(id=pk)[:4]
    detailspage = shoppagemodel.objects.all()
    details_tags = Tags.objects.all()
    product_version = Product_version.objects.all()
    product_img = Product_version.objects.filter(pk=pk).all()
    form = productform(instance=productdetail)
    reviews = Review.objects.filter(reviews__pk=pk)
    count = Review.objects.filter(reviews=productdetail).count()
    colors = Product_version.objects.values_list("details_color__name", 'product__id').distinct().values('details_color__name', 'product__id').annotate(count = Count('details_color__name'))

    if request.method == "POST":
        form = productform(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.reviews = productdetail
            review.save()
            return redirect("mehsullar", pk=pk)
    else:
        form = productform()

    context = {
        "title": "shoppage",
        "detailspage": detailspage,
        "productdetail": productdetail,
        "related": related_products,
        "form": form,
        "reviews": reviews,
        "count": count,
        "details_tags": details_tags,
        "product_img": product_img,
        "product_version": product_version,
        "colors": colors
    }
    return render(request, "product-details.html", context=context)


def shoppage(request):
    shops = shoppagemodel.objects.all()
    page = Paginator(shops,1)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    categories = Category.objects.all()
    manufacturer = Manufacturer.objects.all()
    colors = Category_color.objects.all()

    context = {
        "title": "crops",
        "shops": shops,
        "categories": categories,
        "manufacturer": manufacturer,
        "colors": colors,
        'page':page

    }
    return render(request, "shop-grid-left-sidebar-4-column.html", context=context)


def shoppage_1(request, slug):
    shops = shoppagemodel.objects.filter(Category__slug=slug)
    page = Paginator(shops,1)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    categories = Category.objects.all()
    manufacturer = Manufacturer.objects.all()
    colors = Category_color.objects.all()

    context = {
        "title": "crops",
        "categories": categories,
        "shops": shops,
        "manufacturer": manufacturer,
        "colors": colors,
        'page':page
    }
    return render(request, "shop-grid-left-sidebar-4-column.html", context=context)


def shoppage_2(request, slug):
    shops = shoppagemodel.objects.filter(Manufacturer__slug=slug)
    page = Paginator(shops,1)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    categories = Category.objects.all()
    manufacturer = Manufacturer.objects.all()
    colors = Category_color.objects.all()

    context = {
        "title": "crops",
        "shops": shops,
        "categories": categories,
        "manufacturer": manufacturer,
        "colors": colors,
        'page':page
    }
    return render(request, "shop-grid-left-sidebar-4-column.html", context=context)


def shoppage_3(request, slug):
    shops = shoppagemodel.objects.filter(category_color__slug=slug)
    page = Paginator(shops,1)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    categories = Category.objects.all()
    manufacturer = Manufacturer.objects.all()
    colors = Category_color.objects.all()

    context = {
        "title": "crops",
        "shops": shops,
        "categories": categories,
        "manufacturer": manufacturer,
        "colors": colors,
        'page':page
    }
    return render(request, "shop-grid-left-sidebar-4-column.html", context=context)
