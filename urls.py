from rest_framework import routers
from OhhRazomApi.views import NewApi

router = routers.DefaultRouter()
router.register('api/v1/rk', NewApi, 'new')

urlpatterns = router.urls