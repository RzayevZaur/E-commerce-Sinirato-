from django.urls import path

from . import views


urlpatterns =[
    path ("cart/", views.order, name='cart'),
    path ("checkout/",views.orders,name='checkout')

]

