from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'retail/index.html')

def login(request):
    return render(request, 'retail/login.html')

@login_required
def agent(request):
    return render(request, 'retail/agent/index.html')

@login_required
def retailer(request):
    return render(request, 'retail/retailer/index.html')