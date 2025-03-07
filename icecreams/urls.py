from django.urls import path
from django.views.generic import TemplateView

app_name = "icecreams"

urlpatterns = [
    path("", TemplateView.as_view(template_name="icecreams/home.html"), name="home"),
]