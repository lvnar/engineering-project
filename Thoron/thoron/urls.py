from rest_framework import routers

from thoron.vehicles.views import VehicleViewSet
from thoron.users.views import UserViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'vehicles', VehicleViewSet)

urlpatterns = router.urls
