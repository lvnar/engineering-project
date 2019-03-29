from rest_framework.viewsets import GenericViewSet
from geb.mixins import (ListModelMixin,
                        CreateModelMixin,
                        RetrieveModelMixin,
                        UpdateModelMixin)



class CustomViewSet(GenericViewSet,
                    ListModelMixin,
                    RetrieveModelMixin,
                    UpdateModelMixin,
                    CreateModelMixin):

    pass
