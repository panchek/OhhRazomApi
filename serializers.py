from rest_framework import serializers
from .models import *

class SidePlanesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SidePlanes
        fields = '__all__'
