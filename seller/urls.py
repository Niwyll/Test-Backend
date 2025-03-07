from django.urls import path, include
from seller.views import HomeView, OrderCreateView

app_name = "seller"

urlpatterns = [
    path("api/", include("seller.api.urls")),
    path("", HomeView.as_view(), name="home"),
    path("orders/create/", OrderCreateView.as_view(), name="order-create")
]