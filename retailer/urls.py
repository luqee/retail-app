from django.urls import path
from .views import OutletView, SearchView, TransactionsList, GetUserView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('auth/', jwt_views.TokenObtainPairView.as_view(), name='authenticate'),
    path('auth/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('transactions/', TransactionsList.as_view(), name='trans_list'),
    path('outlet/', OutletView.as_view(), name='get_outlet'),
    path('user/', GetUserView.as_view(), name='get_user'),
    path('products/search/', SearchView.as_view(), name='search_product'),
]