from rest_framework.authentication import TokenAuthentication
from rest_auth.views import LogoutView


class CustomLogoutView(LogoutView):
    authentication_classes = (TokenAuthentication,)
