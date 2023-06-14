from django.urls import path
from . import views

urlpatterns = [
    path('mainPage/', views.mainPage, name='main'),
    path('news/', views.news, name='news'),
    path('store/', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
]
