
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
from django.db.models import Sum, Count, Case, When, DecimalField


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


# class GetAutoCompleteList(APIView):
#     # permission_classes = (IsAuthenticated,)
#     serializer_class = RkCompanySerializer
#
#     def get(self, request, rk_name, filter_type_name, *args, **kwargs):
#         # if request.user.is_authenticated:
#         # if rk_name is not 'null':
#             MAPPING = {
#                         'Razom_number__city_standart': 'id',
#                         'Razom_number__city_standart__city_standart_UA': 'value_name',
#                         'Razom_number__format': 'id',
#                         'Razom_number__format__format': 'value_name',
#                        }
#             if filter_type_name == 'city':
#                 data = RkCompany.objects.filter(rk__RK=rk_name)\
#                         .values(
#                             'Razom_number__city_standart__city_standart_UA',
#                             'Razom_number__city_standart')
#
#             elif filter_type_name == 'format':
#                 data = RkCompany.objects.filter(rk__RK=rk_name)\
#                         .values(
#                             'Razom_number__format',
#                             'Razom_number__format__format')
#             # print('000000', data)
#             data = list(data)
#             list1 = []
#             for i in data:
#                 ne = {MAPPING[key]: value for key, value in i.items()}
#                 list1.append(ne)
#             # print(list1)
#             res = list({i['id']: i for i in list1}.values())
#
#
#             # serializer = RkCompanySerializer(data, many=True)
#             return JsonResponse({'data': res})


class GetAutoCompleteList(APIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = RkCompanySerializer


    def post(self, request, *args, **kwargs):
            rk_name = request.data['rk_name']
            city_name = request.data['city_name'].split(',')
            format_name = request.data['format_name'].split(',')
            filter_type_name = request.data['filter_type_name']

            MAPPING = {
                        'Razom_number__city_standart': 'id',
                        'Razom_number__city_standart__city_standart_UA': 'value_name',
                        'Razom_number__format': 'id',
                        'Razom_number__format__format': 'value_name',
                       }
            data = RkCompany.objects\
                .filter(rk__RK=rk_name)

            if city_name[0] != 'zer0':
                data = data \
                    .filter(Razom_number__city_standart__city_standart_UA__in=city_name)
            if format_name[0] != 'zer0':
                data = data \
                    .filter(Razom_number__format__format__in=format_name)

            if filter_type_name == 'city':
                data = data\
                        .values(
                            'Razom_number__city_standart__city_standart_UA',
                            'Razom_number__city_standart')

            elif filter_type_name == 'format':
                data = data\
                        .values(
                            'Razom_number__format',
                            'Razom_number__format__format')
            # print('000000', data)
            data = list(data)
            list1 = []
            for i in data:
                ne = {MAPPING[key]: value for key, value in i.items()}
                list1.append(ne)
            # print(list1)
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





class GetData(APIView):
    serializer_class = RkCompanySerializer

    def post(self, request, *args, **kwargs):
        print(request.data)
        rk_name = request.data['rk_name']
        city_name = request.data['city_name'].split(',')
        format_name = request.data['format_name'].split(',')
        # type_name = request.data['type_name']

        try:

            data = RkCompany.objects \
                .filter(rk__RK=rk_name)

            if city_name[0] != 'zer0':
                data = data \
                    .filter(Razom_number__city_standart__city_standart_UA__in=city_name)
            if format_name[0] != 'zer0':
                data = data \
                    .filter(Razom_number__format__format__in=format_name)
                # if type_name is not None:
                #     data = data \
                #         .filter(Razom_number__type__typeUA=type_name)
            serializer = RkCompanySerializer(data, many=True)
            return Response(serializer.data)

        except:
            print('Oopps')

class GetCabinetInfo(APIView):


    def get(self, request, *args, **kwargs):
        dataClient = Client.objects.filter(founder_id=request.user.id) \
                    .values(
                        'client',
                        'agancy__Agancy',
                        'founder__username',
                        'isActive',
                        'permisionusersclient__userId__username',
                        'permisionusersclient__userId__last_login',
                        'permisionusersclient__userId__date_joined',
                    )\
                    .annotate(total_budget=Sum('rk__rkcompany__price')) \
                    .annotate(total_product_count=Count('rk__rkcompany')) \
                    .annotate(total_story_count=Count('rk__rkcompany__story', distinct=True)) \
                    .annotate(total_rk_count=Count('rk',  distinct=True))

        dataRK = Rk.objects.filter(client__founder__id=request.user.id) \
            .values(
                'id',
                'RK',
                'client__client',
                'client__agancy__Agancy',
                'client__founder__username',
                'Stage',
                'create_date',
                'end_date',
            ) \
            .annotate(total_budget=Sum('rkcompany__price')) \
            .annotate(total_story_count=Count('rkcompany__story', distinct=True)) \
            .annotate(total_product_count=Count('rkcompany')) \
            .annotate(total_like_count=Sum(Case(When(rkcompany__Grade=1, then=F('rkcompany__Grade')) \
                                                , default=0))) \
            .annotate(total_dislike_count=Sum(Case(When(rkcompany__Grade=2, then=F('rkcompany__Grade')) \
                                                , default=0))) \
            # Sum(Case(When(stock__ttype='I', then=F('stock__quantity')), output_field=DecimalField(), default=0))

        json_response = {'dataClient': list(dataClient),
                          'dataRK': list(dataRK)}
        print(json_response)
        return JsonResponse({'data': json_response})

class AdvProductStatistic(APIView):
    def post(self, request, *args, **kwargs):
        # print(request.data)
        request_data = request.data
        responce_data = \
        [
            {
                "Statistica": "Total amount",
                "Value": sum([i["Total_budget"] for i in request_data if i["Total_budget"] != '-']),
                "Description": "-"
            },
            {
                "Statistica": "Total count",
                "Value": sum([i["Total_product_count"] for i in request_data if i["Total_product_count"] != '-']),
                "Description": "-"
            },
            {
                "Statistica": "City",
                "Value":  sum([i[0]for i in list(Rk.objects \
                    .filter(pk__in=[i["id"] for i in request_data])
                    .annotate(total_city_count=Count('rkcompany__Razom_number__city_standart__city_standart_UA', distinct=True))
                    .values_list("total_city_count"))]),
                "Description": list(Rk.objects \
                        .filter(pk__in=[i["id"] for i in request_data if i["Total_story_count"] != '-'])
                        .values_list("rkcompany__Razom_number__city_standart__city_standart_UA").distinct())
            },
        ]
        print(responce_data)
        return JsonResponse({'data': responce_data})

class ViewActionDetails(APIView):
    def post(self, request, *args, **kwargs):
        request_data = request.data
        response_data = RkCompany.objects\
                            .filter(rk__id__in=[i["id"] for i in request_data]) \
                            .exclude(comment__isnull=True) \
                            .values(
                                "Razom_number__Razom_number",
                                "rk__RK",
                                "comment",
                            )
        print(response_data)
        return JsonResponse({'data': list(response_data)})



