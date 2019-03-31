from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.views import exception_handler
from rest_framework.response import Response


def custom_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        try:
            message = _(response.data['detail'])
        except:
            message = _(response.status_text)
        return Response(
            {
                "status": response.status_code,
                "message": message
            },
            response.status_code
        )
    return response
