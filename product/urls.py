from django.urls import path

from. import views

urlpatterns = [
    path("product-details/<int:pk>/",views.details, name='mehsullar'),
    path("shop/",views.shoppage,name='crops'),
    path("shop/category/<slug:slug>/",views.shoppage_1,name='productcategory'),
    path("shop/manufacturer/<slug:slug>/",views.shoppage_2,name='productManufacturer'),
    path("shop/color/<slug:slug>/",views.shoppage_3,name='productcolor'),
    # path("shop/detailcolors/<int:pk>/",views.details_1,name='productdetailscolor')

    
]


 

