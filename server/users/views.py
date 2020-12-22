from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .serializer import UserSerializer
from .models import User
from classes.models import Class, Post, Comment

import json
from ast import literal_eval
class UserHandler(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    
    def calculate_similar(self, user):
        mentors = User.objects.filter(user_type="MR").values('id', 'first_name', 'last_name', 'qualification', 'organization', 'requirement', 'duration')

        recommendations = []

        for obj in mentors:
            mentor_score = 0

            mentor_duration = int(obj['duration'])
            mentor_qualification = obj['qualification']
            mentor_requirement = set(obj['requirement'].replace(' ', '').lower().split(','))

            user_req = set(user.requirement.replace(' ', '').lower().split(','))
            user_dur = int(user.duration)
            num_common = len(mentor_requirement.intersection(user_req))
            
            mentor_score += 5*num_common

            time_diff = abs(mentor_duration - user_dur)
            if time_diff in range(2):
                mentor_score += 5
            elif time_diff in range(3, 5):
                mentor_score += 3
            else:
                mentor_score += 1
            
            recommendations.append({ 'id': obj['id'],
                                        'first_name': obj['first_name'],
                                        'last_name': obj['last_name'],
                                        'qualification': obj['qualification'],
                                        'organization': obj['organization'],
                                        'requirement': obj['requirement'],
                                        'duration': obj['duration'],
                                        'score': mentor_score,
                                        })
                                    
        
        print(recommendations)
        return recommendations

    def get(self, request):
        user = request.user
        print(user.first_name, user.email, user.duration, user.qualification, user.user_type, user.organization, user.requirement, user.classes)
        classes = Class.objects.filter(mentor_id=user.id).values()
        print("classes")
        print(classes)
        mentors = self.calculate_similar(user)

        return Response({
            'first_name': user.first_name, 'email': user.email, 'duration': user.duration, 'qualification': user.qualification, 'user_type': user.user_type,'organization':  user.organization, 'requirement': user.requirement, 'classes': classes, 'mentorData': mentors 
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



class MentorMatching(APIView):
    authentication_classes = [authentication.TokenAuthentication]

    def calculate_similar(user):
        duration = user.duration
        requirement = user.requirement
        mentors =  User.objects.filter(user_type="MR")

        print(mentors)
        
        return "random"
    
    def get(self, request):
        user = request.user
        recommendations = calculate_similar(user)

        return Response({'data': recommendations})
