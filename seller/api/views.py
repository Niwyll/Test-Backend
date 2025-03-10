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

    def cancel_order(self):
        pass

    def create(self, request, *args, **kwargs):
        order = None
        items = []
        for key, value in request.data['items'].items():
            # Skipping empty values
            if not value:
                continue

            # Singleton to create Order to avoid empty values
            if not order:
                order = Order.objects.create()

            ice_cream = IceCream.objects.get(name=key)
            bucket = IceCreamBucket.objects.get(ice_cream=ice_cream)
            if value > bucket.quantity:
                self.cancel_order()
                return Response(
                    {"error": f"Not enough ice cream in {bucket.ice_cream.name} bucket to make {value} balls ({bucket.quantity} remaining)"},
                    status=status.HTTP_422_UNPROCESSABLE_ENTITY
                )
            bucket.quantity -= value
            bucket.save()
            ice_cream_ball = IceCreamBall.objects.create(ice_cream=ice_cream, quantity=value)
            item = Item.objects.create(item_ref=ice_cream_ball, order=order, price=200)
            items.append(item)

        if not order:
            return Response(
                {"error": f"No items selected"},
                status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )

        return Response({
            "uuid": order.uuid,
        }, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, *args, **kwargs):
        order = Order.objects.get(uuid=kwargs['pk'])
        return Response({
            "items": [
                {
                    "name": item.item_ref.ice_cream.name,
                    "quantity": item.item_ref.quantity,
                    "image_ref": item.item_ref.ice_cream.image_path
                }
                for item in order.item_set.all()
            ]
        })