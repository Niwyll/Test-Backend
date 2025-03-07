from rest_framework.response import Response
from rest_framework.views import APIView
from icecreams.models import IceCream
from icecreams.api.serializers import IceCreamSerializer

class IceCreamListView(APIView):
    """API endpoint to get available ice cream choices."""

    def get(self, request):
        icecreams = IceCream.objects.all()
        serializer = IceCreamSerializer(icecreams, many=True)
        return Response(serializer.data)