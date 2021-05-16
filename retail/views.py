from django.shortcuts import render, redirect
from django.views.generic import CreateView
from retail.models import User
from retail.forms import RetailerCreateForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

def index(request):
    return render(request, 'retail/index.html')

# def login(request):
#     return render(request, 'retail/login.html')

@login_required
def recruiter(request):
    return render(request, 'retail/recruiter/index.html')

# Route to create Retailer
@method_decorator([login_required,], name='dispatch')
class RetailerCreateView(CreateView):
    model = User
    form_class = RetailerCreateForm
    template_name = 'retail/recruiter/retailer.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'retailer'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        user = form.save()
        return redirect('recruiter')

# Route to create Outlet
def create(request):
    return render(request, 'retail/recruiter/outlet.html')

