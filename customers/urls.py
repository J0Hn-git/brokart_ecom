from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('accounts',views.show_account,name='account'),
    path('logout',views.sign_out,name='logout')
]

   

