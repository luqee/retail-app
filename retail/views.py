from django.shortcuts import render

def index(request):
    return render(request, 'retail/index.html')

def login(request):
    return render(request, 'retail/login.html')

def recruiter(request):
    return render(request, 'retail/recruiter/index.html')
