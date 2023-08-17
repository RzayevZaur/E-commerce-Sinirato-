from django.urls import path

from. import views

urlpatterns = [
    path("details/",views.details, name='mehsullar'),
    path("shop/",views.shoppage,name='crops'),
    path("shop/<str:category>/",views.shoppage_1,name='productcategory'),
    path("shop/<str:Manufacturer>/",views.shoppage_2,name='productManufacturer')
]


 

