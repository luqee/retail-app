from django.urls import path
from .views import TransactionsList, GetUserView
urlpatterns = [
    path('trans/', TransactionsList.as_view(), name='trans_list'),
    path('trans/user', GetUserView.as_view(), name='get_user'),
]