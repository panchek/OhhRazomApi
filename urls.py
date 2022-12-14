from OhhRazomApi.views import *
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/getrk', GetRK.as_view()),
    path('api/getautocompletelist', GetAutoCompleteList.as_view()),
    path('api/getstat', GetStat.as_view()),

    path('api/getalldata', GetData.as_view()),
    path('api/getcabinetinfo', GetCabinetInfo.as_view()),
    path('api/advproductstatistic', AdvProductStatistic.as_view()),
    path('api/viewactiondetails', ViewActionDetails.as_view()),
    path('api/addproduct' , AddNewProduct.as_view()),
    path('api/deleterk', DeleteRK.as_view()),
    path('api/getrksettings/<str:rk>', GetRkSettings.as_view()),
    path('api/getrksettings/plusimg/<str:rk>', GetRkSettingsWithImg.as_view()),
    path('api/addnewrk', AddNewRk.as_view()),
    path('api/deleterk2', DeleteRK_2.as_view()),
    path('api/changeprice', ChangePrice.as_view()),
    path('api/exportexcel', ExportToExcel.as_view()),

    path('api/rktest', StoryTestApi.as_view()),
    path('api/rktest/2', StoryTestApi2.as_view()),
    path('api/rkposttest', RkTestApi.as_view()),
    path('api/filterdata', CityApi.as_view()),
    path('api/logout', LogOut.as_view()),
    path('api/login', LogIn.as_view()),
]