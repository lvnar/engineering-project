from .models import Vehicle
from rest_framework import viewsets, response, status
from .serializers import VehicleSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows vehicles to be viewed or edited.
    """
    queryset = Vehicle.objects.all().order_by('-date_joined')
    serializer_class = VehicleSerializer
    filterset_fields = ('is_active', 'owner__id')
    
    def destroy(self, request, *args, **kwargs):
        vehicle = self.get_object()
        vehicle.is_active = False
        vehicle.save()

        return response.Response(None, status.HTTP_204_NO_CONTENT)