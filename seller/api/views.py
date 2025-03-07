from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from seller.models import Order
from seller.api.serializers import OrderSerializer

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer