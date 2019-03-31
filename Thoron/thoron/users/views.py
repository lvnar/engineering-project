from django.contrib.auth.models import User
from rest_framework import viewsets, response, status, permissions
from utils.customPermissions import IsSuperUser
from thoron.vehicles.models import Vehicle
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (permissions.IsAuthenticated, IsSuperUser)
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    filterset_fields = ('is_active',)
    
    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        user.is_active = False
        Vehicle.objects.filter(owner=user).update(is_active=False)
        user.save()

        return response.Response(None, status.HTTP_204_NO_CONTENT)
