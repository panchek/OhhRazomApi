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
    path('api/rktest', StoryTestApi.as_view()),
    path('api/rktest/2', StoryTestApi2.as_view()),
    path('api/rkposttest', RkTestApi.as_view()),
]