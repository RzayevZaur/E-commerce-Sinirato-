from django.urls import path

from . import views


urlpatterns =[
    path ("command/", views.order, name='command'),
    path ("direction/",views.orders,name='direction')

]

