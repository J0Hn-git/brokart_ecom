from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('cart',views.show_cart, name='cart'),
]

