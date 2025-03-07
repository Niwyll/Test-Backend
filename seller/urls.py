from django.urls import path, include
from seller.views import HomeView, OrderCreateView, OrderDetailView, OrderConfirmationView

app_name = "seller"

urlpatterns = [
    path("api/", include("seller.api.urls")),
    path("", HomeView.as_view(), name="home"),
    path("orders/create/", OrderCreateView.as_view(), name="order-create"),
    path("orders/<uuid:order_uuid>/", OrderDetailView.as_view(), name="order-detail"),
    path("orders/<uuid:order_uuid>/confirm/", OrderConfirmationView.as_view(), name="order-confirmation"),
]