from django.urls import path
from .views import CustomLoginView, myaccount, RegisterView, activate
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("myaccount/", myaccount, name="myaccount"),
    path("confirmation/<str:uidb64>/<str:token>/", activate, name="confirmation"),
    path("register/", RegisterView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
