from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .serializer import UserSerializer
import json
class UserHandler(APIView):
    authentication_classes = [authentication.TokenAuthentication]

    def get(self, request):
        user = request.user
        print(user.first_name, user.email, user.duration, user.qualification, user.user_type, user.organization, user.requirement, user.classes)


        return Response({
            'first_name': user.first_name, 'email': user.email, 'duration': user.duration, 'qualification': user.qualification, 'user_type': user.user_type,'organization':  user.organization, 'requirement': user.requirement, 'classes': user.classes
        })


class UserCompleteProfile(APIView):
    authentication_classes = [authentication.TokenAuthentication]

    def post(self, request):
        user = request.user
        data = json.loads(request.body)
        print(data)
        for attr, value in data.items():
            print(attr,value)
            setattr(user, attr, value)

        user.save()
        return Response({'data': user.first_name})

class MentorCreation(APIView):
    authentication_classes = [authentication.TokenAuthentication]

    def post(self, request):
        user = request.user
        data = json.loads(request.body)
        for attr, value in data.items():
            print(attr,value)
            setattr(user, attr, value)
        
        user.user_type = 'MR'

        user.save()
        print(data)
        return Response({'data' : 200})



