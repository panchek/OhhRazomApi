from rest_framework import serializers
from .models import *


class AdressPlanesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdressPlanes
        fields = '__all__'

class CityPlanesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityPlanes
        fields = '__all__'

class TypePlanesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypePlanes
        fields = '__all__'

class FormatPlanesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormatPlanes
        fields = '__all__'

class SidePlanesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SidePlanes
        fields = '__all__'

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = '__all__'

class TotalplanesSerializer(serializers.ModelSerializer):
    city_standart = CityPlanesSerializer()
    adress = AdressPlanesSerializer()
    type = TypePlanesSerializer()
    format = FormatPlanesSerializer()
    side = SidePlanesSerializer()
    class Meta:
        model = Totalplanes
        fields = '__all__'

class RkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rk
        fields = '__all__'

class RkCompanySerializer(serializers.ModelSerializer):
    Razom_number = TotalplanesSerializer()
    story = StorySerializer()
    class Meta:
        model = RkCompany
        fields = '__all__'
