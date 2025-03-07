from django.urls import path, include
from rest_framework.routers import DefaultRouter
from seller.api.views import OrderViewSet

router = DefaultRouter()
router.register("orders", OrderViewSet)

urlpatterns = [
    path("", include(router.urls)), 
]