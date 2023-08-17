from django.urls import path

from . import views

urlpatterns=[
    path("blogone/",views.blogone,name='blogone'),
    path("blog-detalien/<int:pk>/",views.blog,name='blog'),
    path("blogone/<str:category>/",views.blogtwo,name='category'),


]

