
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
# class NewApi(generics.ListCreateAPIView):
#     queryset = SidePlanes.objects.all()
#     serializer_class = SidePlanesSerializer

class StoryTestApi(generics.ListCreateAPIView):
        queryset = RkCompany.objects.filter(rk_id=69)   #32
        serializer_class = RkCompanySerializer

class GetRK(generics.ListCreateAPIView):
        queryset = Rk.objects.filter(client_id=8)
        serializer_class = RkSerializer

class StoryTestApi2(generics.ListCreateAPIView):
        queryset = Totalplanes.objects.filter(Razom_number=64218)
        serializer_class = TotalplanesSerializer

# @api_view(['POST'])
# def postTest(request):
#         if request.method == 'POST':
#                 rk = JSONParser().parse(request)[0]
#                 rk_2 = list(rk.values())[0]
#                 queryset = RkCompany.objects.filter(rk_id=rk_2)
#                 serializer_class = RkSerializer

class RkTestApi(APIView):
        serializer_class = RkCompanySerializer

        def get_queryset(self):
                all_rk = RkCompany.objects.all()
                return all_rk
        # def get(self,request, *args, **kwargs):
        #         newRk = self.get_queryset()
        #         serializer = RkCompanySerializer(newRk, many=True)
        #         return Response(serializer.data)

        def post(self, request, *args, **kwargs):
                print(request.data)
                rk = list(request.data.values())[0]
                # rk = json.loads(request.data)
                new = RkCompany.objects.filter(rk__RK=rk)
                serializer = RkCompanySerializer(new, many=True)
                return Response(serializer.data)