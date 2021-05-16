from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='retail/login.html')),
    path('recruiter/', views.recruiter, name='recruiter'),
    path('recruiter/retailer/', views.RetailerCreateView.as_view(), name='retailer.create'),
]
