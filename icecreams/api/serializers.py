from rest_framework import serializers
from icecreams.models import IceCream


class IceCreamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IceCream
        fields = ('name',)