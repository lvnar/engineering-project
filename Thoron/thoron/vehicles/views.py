import re

from rest_framework import viewsets, response, status, permissions
from .models import Vehicle
from .serializers import VehicleSerializer
from utils.customPermissions import IsOwner

class VehicleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows vehicles to be viewed or edited.
    """
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    queryset = Vehicle.objects.all().order_by('-date_joined')
    serializer_class = VehicleSerializer
    filterset_fields = ('is_active', 'owner__id')

    list_pattern = re.compile('^/vehicles/$')

    def get_queryset(self, *args, **kwarg):
        if self.request.method == 'GET' and \
           self.request.user.is_superuser != True and \
           self.list_pattern.match(self.request.path):
            return Vehicle.objects.filter(
                owner=self.request.user,
                is_active=True
            ).order_by('-date_joined')
        return self.queryset

    def destroy(self, request, *args, **kwargs):
        vehicle = self.get_object()
        vehicle.is_active = False
        vehicle.save()

        return response.Response(None, status.HTTP_204_NO_CONTENT)
