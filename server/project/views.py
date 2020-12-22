from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
# Create your views here.


class ProjectHandler(APIView):
    authentication_classes = [authentication.TokenAuthentication]

    def post(self, request):
        name = request.body.name
        return Response({})