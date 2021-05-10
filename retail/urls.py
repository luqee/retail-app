from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    # path('login', auth_views.LoginView.as_view(template_name='retail/login.html'), name='login'),
    path('agent', views.agent, name='agent'),
    path('retailer', views.retailer, name='retailer'),
]
