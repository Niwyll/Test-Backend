from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, TemplateView

from seller.forms import OrderSearchForm
from seller.models import Order
from icecreams.models import IceCream

class RegisterView(CreateView):
    template_name = "registration/register.html"  # Your template
    form_class = UserCreationForm  # Built-in form
    success_url = reverse_lazy("login")  # Redirect to login page after successful registration

class HomeView(FormView):
    template_name = "seller/home.html"
    form_class = OrderSearchForm

class OrderCreateView(TemplateView):
    template_name = "seller/order_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['icecreams'] = IceCream.objects.all()
        return context