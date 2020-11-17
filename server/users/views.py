from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions


class UserHandler(APIView):
    authentication_classes = [authentication.TokenAuthentication]

    def get(self, request):
        user_token = request.user
        print(user_token.first_name)
        return Response({"message": user_token.first_name})


