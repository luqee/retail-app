from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='retail/login.html')),
    path('recruiter/', views.recruiter, name='recruiter'),
    path('retailer/create/', views.RetailerCreateView.as_view(), name='retailer.create'),
    path('outlet/create/', views.CreateOuteltView.as_view(), name='outlet.create'),
]
