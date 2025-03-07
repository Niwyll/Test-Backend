from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from icecreams.models import IceCream, IceCreamBall, IceCreamBucket
from seller.models import Order, Item
from seller.api.serializers import OrderSerializer

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        order = Order.objects.create()
        items = []
        for key, value in request.data['items'].items():
            ice_cream = IceCream.objects.get(name=key)
            ice_cream_ball = IceCreamBall.objects.create(ice_cream=ice_cream, quantity=value)
            item = Item.objects.create(item_ref=ice_cream_ball, order=order, price=200)
            items.append(item)
        return Response({
            "uuid": order.uuid,
            "price": round(sum([item.price * item.item_ref.quantity for item in items]) / 100, 2)
        }, status=status.HTTP_201_CREATED)