from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('agent', views.agent, name='agent'),
    path('retailer', views.retailer, name='retailer'),
]
