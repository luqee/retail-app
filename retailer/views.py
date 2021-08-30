from retailer.models import Transaction
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from retail.models import Outlet, Product
from .serializers import ProductSerializer, RetailerSerializer, TransactionSerializer, OutletSerializer

class GetUserView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        data = RetailerSerializer(user.retailer).data
        return Response({"retailer": data})

class OutletView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        outlets = user.retailer.outlets
        data = OutletSerializer(outlets, many=True).data
        return Response(data)

# View list of all transactions
class TransactionsList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TransactionSerializer
    
    def get_queryset(self):
        user = self.request.user
        transactions = Transaction.objects.filter(outlet__owner=user.retailer).all()
        return transactions
    
    def post(self, request):
        user = request.user
        outlet = Outlet.objects.get(pk=request.data['outlet'])
        product = Product.objects.get(pk=request.data['product'])
        transaction = Transaction.objects.create(outlet=outlet, product=product, quantity=request.data['quantity'], tran_type=request.data['tran_type'])
        data = TransactionSerializer(transaction).data
        return Response(data)

class SearchView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        barcode = request.GET.get('q', '')
        product = Product.objects.filter(bar_code__icontains=barcode).first()
        data = ProductSerializer(product).data
        return Response(data)