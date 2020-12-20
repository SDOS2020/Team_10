from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .models import Class
import json

class ClassHandler(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    
    def post(self,request):
        user = request.user
        data = json.loads(request.body)
        mentorClass = Class(title=data['className'], description=data['classText'], tags=data['classTopics'], mentor=user)
        mentorClass.save()
        return Response({'data': 200})