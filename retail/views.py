from django.shortcuts import render, redirect
from django.views.generic import CreateView
from retail.models import Outlet, Retailer, User
from retail.forms import OutletForm, RetailerCreateForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils.text import slugify

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

    # def get_context_data(self, **kwargs):
    #     kwargs['user_type'] = 'retailer'
    #     return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        user = form.save()
        Retailer.objects.create(user=user, mobile=form.cleaned_data.get('mobile'), registered_by=self.request.user.recruiter)
        return redirect('recruiter')

# Route to create Outlet
@method_decorator([login_required,], name='dispatch')
class CreateOuteltView(CreateView):
    model = Outlet
    form_class = OutletForm
    template_name = 'retail/recruiter/outlet.html'
    success_url = '/recruiter/'

    def form_valid(self, form):
        form.instance.slug = slugify(form.cleaned_data.get('name'))
        form.instance.registered_by = self.request.user.recruiter
        form.instance.location = self.request.POST['location_0']
        form.instance.latitude = self.request.POST['location_1']
        form.instance.longitude = self.request.POST['location_2']
        return super().form_valid(form)
        

