from rest_framework import routers
from .api import ProyectViewSet

router = routers.DefaultRouter()
router.register('api/proyects', ProyectViewSet, 'proyects')

urlpatterns = router.urls
