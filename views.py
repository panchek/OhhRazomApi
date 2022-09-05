
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated


class StoryTestApi(generics.ListCreateAPIView):
        queryset = RkCompany.objects.filter(rk_id=69)   #32
        serializer_class = RkCompanySerializer

# class GetRK(generics.ListCreateAPIView):
#         queryset = Rk.objects.filter(client_id=8)
#         serializer_class = RkSerializer
class GetRK(APIView):
        # permission_classes = (IsAuthenticated,)
        serializer_class = RkSerializer

        def get(self, request, *args, **kwargs):
                # if request.user.is_authenticated:
                        data = Rk.objects.filter(client__founder__id=request.user.id)
                        serializer = RkSerializer(data, many=True)
                        return Response(serializer.data)


class StoryTestApi2(generics.ListCreateAPIView):
        queryset = Totalplanes.objects.filter(Razom_number=64218)
        serializer_class = TotalplanesSerializer


class RkTestApi(APIView):
        permission_classes = (IsAuthenticated,)
        serializer_class = RkCompanySerializer

        def get_queryset(self):
                all_rk = RkCompany.objects.all()
                return all_rk
        # def get(self,request, *args, **kwargs):
        #         newRk = self.get_queryset()
        #         serializer = RkCompanySerializer(newRk, many=True)
        #         return Response(serializer.data)

        def post(self, request, *args, **kwargs):
                if request.user.is_authenticated:
                        print(request.data)
                        rk = list(request.data.values())[0]
                        new = RkCompany.objects.filter(rk__RK=rk)
                        serializer = RkCompanySerializer(new, many=True)
                        return Response(serializer.data)

# class LogOut(APIView):
#         def get(self, request, format=None, *args, **kwargs):
#
#                 print(request.user.is_authenticated)
#                 request.auth.auth_token.delete()
#                 return Response(status=status.HTTP_200_OK)

class LogIn(APIView):

        def get(self, request, *args, **kwargs):
                if request.user.is_authenticated:
                        return Response(status=status.HTTP_200_OK)
                else:
                        return Response(status=status.HTTP_401_UNAUTHORIZED)


class LogOut(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)