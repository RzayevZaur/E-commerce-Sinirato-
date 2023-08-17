from django.shortcuts import render, redirect, get_object_or_404

from .forms import blogforms
from .models import blogp, Category, comment,Tags

# Create your views here.


def blog(request, pk):
    blogdetail = get_object_or_404(blogp, pk=pk)
    all = blogp.objects.order_by("-created").all()
    categories = Category.objects.all()
    comments = comment.objects.filter(blog__pk=pk)
    
    if request.method == "POST":
        form = blogforms(request.POST)
        if form.is_valid():
            comments = form.save(commit=False)
            comments.blog = blogdetail
            comments.save()
            return redirect("blog", pk=pk)
    else:
        form = blogforms()

    context = {
        "title": "blog page",
        "all": all,
        "form": form,
        "blogdetail": blogdetail,
        "categories": categories,
        "comments": comments,
    }

    return render(request, "blog-details.html", context=context)


def blogone(request):
    allblog = blogp.objects.order_by("-created").all()
    categories = Category.objects.all()
    tag=Tags.objects.all()

    context = {"title": "blog page one", "allblog": allblog, "categories": categories,"tag":tag}

    return render(request, "blog-right-sidebar-3.html", context=context)


def blogtwo(request, category):
    all = blogp.objects.filter(category__name=category).all()
    categories = Category.objects.all()
    tag=Tags.objects.all()
    context = {"title": "blog page one", "allblog": all,"categories": categories,"tag":tag}
    return render(request, "blog-right-sidebar-3.html", context=context)
