from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, TemplateView, DetailView

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

class OrderDetailView(DetailView):
    model = Order

    def get_object(self, queryset=None):
        order = self.model.objects.get(uuid=self.kwargs['order_uuid'])
        return order

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = [{
            "name": item.item_ref.ice_cream.name,
            "quantity": item.item_ref.quantity,
            "image_path": item.item_ref.ice_cream.image_path,
            "price_per_unit": round(item.price / 100, 2),
            "total_price": item.item_ref.quantity * round(item.price / 100, 2)
        } for item in self.object.item_set.all()]
        context['order_total_price'] = self.object.total_price
        return context

class OrderConfirmationView(TemplateView):
    template_name = "seller/order_confirmation.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order_uuid = self.kwargs['order_uuid']
        context['uuid'] = order_uuid
        order = Order.objects.get(uuid=order_uuid)
        context['price'] = round(
            sum([
                item.price * item.item_ref.quantity
                for item in order.item_set.all()
            ]) / 100,
            2
        )
        return context