from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .decorators import agent_required, retailer_required

# Create your views here.
def index(request):
    return render(request, 'retail/index.html')

def login(request):
    return render(request, 'retail/login.html')

@login_required
@agent_required
def agent(request):
    return render(request, 'retail/agent/index.html')

def retailer(request):
    return render(request, 'retail/retailer/index.html')