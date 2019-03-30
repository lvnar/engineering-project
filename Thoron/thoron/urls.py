from django.urls import include, path
from rest_framework import routers

from thoron.auth.views import CustomLogoutView
from thoron.vehicles.views import VehicleViewSet
from thoron.users.views import UserViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'vehicles', VehicleViewSet)

urlpatterns = [
    path(r'', include('rest_auth.urls')),
    path(r'logout/', CustomLogoutView.as_view())
] + router.urls
