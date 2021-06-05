from retail.models import Product, User
from rest_framework.response import Response
from rest_framework import generics, serializers, status
from rest_framework.views import APIView

from .models import Transaction, Outlet
from .serializers import ProductSerializer, TransactionSerializer, OutletSerializer, UserSerializer

# Create your views here.

class GetUserView(APIView):
    def get(self, request):
        user = User.objects.get(id=1)
        data = UserSerializer(user).data
        return Response({"user": data})

class OutletsView(APIView):
    def get(self, request):
        outlets = Outlet.objects.all()
        data = OutletSerializer(outlets, many=True).data
        return Response(data)

# View list of all transactions
class TransactionsList(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()[:20]
    serializer_class = TransactionSerializer

class SearchView(APIView):
    def get(self, request):
        barcode = request.GET.get('q', '')
        product = Product.objects.filter(bar_code__icontains=barcode).first()
        data = ProductSerializer(product).data
        return Response(data)