from .models import Vehicle
from rest_framework import viewsets
from .serializers import VehicleSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows vehicles to be viewed or edited.
    """
    queryset = Vehicle.objects.all().order_by('id')
    serializer_class = VehicleSerializer