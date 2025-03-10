from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from icecreams.models import IceCream, IceCreamBucket
from icecreams.api.serializers import IceCreamSerializer

class IceCreamListView(APIView):
    """API endpoint to get available ice cream choices."""

    def get(self, request):
        icecreams = IceCream.objects.all()
        serializer = IceCreamSerializer(icecreams, many=True)
        return Response(serializer.data)

class RefillBucketView(APIView):
    """API View to refill an ice cream bucket"""

    def post(self, request, bucket_id):
        bucket = get_object_or_404(IceCreamBucket, id=bucket_id)
        bucket.quantity = bucket.initial_quantity
        bucket.save()

        return Response({
            "message": f"{bucket.ice_cream.name} ice cream bucket refilled to {bucket.quantity}."
        }, status=status.HTTP_200_OK)