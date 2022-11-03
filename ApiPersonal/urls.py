from  rest_framework import routers
from  .api import RegistroviewSet

router = routers.DefaultRouter()
router.register('api/ApiPersonal', RegistroviewSet, 'ApiPersonal')

urlpatterns = router.urls