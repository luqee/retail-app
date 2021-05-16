from django.shortcuts import render
from django.views.generic import CreateView
from retail.models import User
from retail.forms import RetailerCreateForm

def index(request):
    return render(request, 'retail/index.html')

def login(request):
    return render(request, 'retail/login.html')

def recruiter(request):
    return render(request, 'retail/recruiter/index.html')

# Route to create Retailer
class RetailerCreateView(CreateView):
    model = User
    form_class = RetailerCreateForm
    template_name = 'retail/recruiter/retailer.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

# Route to create Outlet
def create(request):
    return render(request, 'retail/recruiter/outlet.html')

