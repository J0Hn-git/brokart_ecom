from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('account',views.show_account, name='account'),
]

