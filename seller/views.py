from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

class RegisterView(CreateView):
    template_name = "registration/register.html"  # Your template
    form_class = UserCreationForm  # Built-in form
    success_url = reverse_lazy("login")  # Redirect to login page after successful registration