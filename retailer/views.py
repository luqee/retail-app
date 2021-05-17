from retail.models import User
from rest_framework.response import Response
from rest_framework import generics, serializers, status
from rest_framework.views import APIView
from django.contrib.auth import authenticate

from .models import Transaction
from .serializers import TransactionSerializer, OutletSerializer, UserSerializer

# Create your views here.

class GetUserView(APIView):
    def get(self, request):
        user = User.objects.get(id=1)
        data = UserSerializer(user).data
        return Response({"user": data})

class LoginView(APIView):

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)

# View list of all transactions
class TransactionsList(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()[:20]
    serializer_class = TransactionSerializer
