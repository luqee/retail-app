from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('recruiter', views.recruiter, name='recruiter'),
    path('recruiter/retailer', views.RetailerCreateView.as_view(), name='retailer.create'),
]
