from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def post_get(request):
    return Response({"message": "Hello, world!"})