from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('cart',views.show_cart, name='cart'),
    path('add_to_cart',views.add_to_cart,name='add_to_cart')
]

