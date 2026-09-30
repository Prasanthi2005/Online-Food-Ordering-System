from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('restaurant/<int:restaurant_id>/', views.restaurantPage, name='restaurantPage'),
]