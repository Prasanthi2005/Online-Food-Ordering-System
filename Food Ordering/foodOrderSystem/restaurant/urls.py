from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.loginRestaurant, name="loginRestaurant"),
    path("register/", views.registerRestaurant, name="registerRestaurant"),
    path("add-menu/", views.addMenu, name="addMenu"),
    path("logout/", views.logoutRestaurant, name="logoutRestaurant"),
]