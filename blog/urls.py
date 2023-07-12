from django.urls import path

from . import views

urlpatterns=[
    path("blogone",views.blog,name='blog'), 
    path("blog",views.blogone,name='blogone')
]

