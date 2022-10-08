
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.db.models import F


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


class GetCity(APIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = RkCompanySerializer

    def get(self, request, rk_name, *args, **kwargs):
        # if request.user.is_authenticated:
        # if rk_name is not 'null':
            mapping = {'Razom_number__city_standart__city_standart_UA':'city',
                   'Razom_number__city_standart': 'id'}
            data = RkCompany.objects.filter(rk__RK=rk_name)\
                    .values(
                        'Razom_number__city_standart__city_standart_UA',
                        'Razom_number__city_standart')
            # print('000000', data)
            data = list(data)
            list1 = []
            for i in data:
                ne = {mapping[key]: value for key, value in i.items()}
                list1.append(ne)
            res = list({i['id']: i for i in list1}.values())


            # serializer = RkCompanySerializer(data, many=True)
            return JsonResponse({'data': res})


class StoryTestApi2(generics.ListCreateAPIView):
        queryset = Totalplanes.objects.filter(Razom_number=64218)
        serializer_class = TotalplanesSerializer


class RkTestApi(APIView):
        permission_classes = (IsAuthenticated,)
        serializer_class = RkCompanySerializer

        def get_queryset(self):
                all_rk = RkCompany.objects.all()
                return all_rk

        def post(self, request, *args, **kwargs):
                if request.user.is_authenticated:
                        rk = list(request.data.values())[0]
                        new = RkCompany.objects.filter(rk__RK=rk)
                        serializer = RkCompanySerializer(new, many=True)
                        return Response(serializer.data)


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

class GetStat(APIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = RkSerializer

    def get(self, request, *args, **kwargs):
        # if request.user.is_authenticated:
        data = RkCompany.objects.filter(rk__client__founder__id=request.user.id)

        rk_list = data.values_list( 'rk__RK')
        city_list = data.values_list( 'Razom_number__city_standart')
        format_list = data.values_list( 'Razom_number__format')
        type_list = data.values_list('Razom_number__type')

        rk_count = len( set( list( rk_list)))
        city_count = len( set( list( city_list)))
        format_count = len(set(list( format_list)))
        type_count = len(set(list( type_list)))
        return Response({
            'rk_count': f'{rk_count}',
            'city_count': f'{city_count}',
            'format_count': f'{format_count}',
            'type_count': f'{type_count}'
        })

class CityApi(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RkCompanySerializer

    def get_queryset(self):
        all_rk = RkCompany.objects.all()
        return all_rk

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            rk_name = request.data['rk_name']
            city_name = request.data['city_name']

            data = RkCompany.objects \
                        .filter(rk__RK=rk_name)  \
                        .filter(Razom_number__city_standart__city_standart_UA=city_name)
            serializer = RkCompanySerializer(data, many=True)
            return Response(serializer.data)