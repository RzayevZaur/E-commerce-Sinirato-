from django.urls import path

from. import views

urlpatterns = [
    path("məhsullar/",views.məhsul, name='vaxt'),
    path ("crops/",views.crop,name='cv'),
    
]




