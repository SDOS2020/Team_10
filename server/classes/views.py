from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .models import Class, Post, Comment
import json

class ClassHandler(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    
    def post(self,request):
        user = request.user
        data = json.loads(request.body)
        mentorClass = Class(title=data['className'], description=data['classText'], tags=data['classTopics'], mentor=user)
        mentorClass.save()
        return Response({'data': 200})
    
    def get(self, request):
        user = request.user
        classes = Class.objects.filter(mentor_id=user.id).values()
        print(classes)

        return Response({'data': classes})

class ClassById(APIView):
    authentication_classes = [authentication.TokenAuthentication]

    def post(self, request):
        data = json.loads(request.body)

        classes = Class.objects.filter(uuid=data['classId']).values()
        return Response(classes)

class PostHandler(APIView):
    authentication_classes = [authentication.TokenAuthentication]

    def post(self, request):

        user = request.user
        data = json.loads(request.body)
        post_class = Class.objects.get(uuid=data['classId'])

        # print(post_class)

        # return Response(post_class)
        new_post = Post(post_text=data['postText'], post_by=user, in_class=post_class)
        new_post.save()

        return Response({'data': 200})
    



class CommentHandler(APIView):
    authentication_classes = [authentication.TokenAuthentication]

    def post(self, request):
        user = request.user
        data = json.loads(request.body)

        comment_text = data['commentText']
        post = Post.objects.get(uuid=data['postId'])

        comment = Comment(parent=post, comment_by=user, comment_text=comment_text)
        comment.save()

        return Response({'data': 200})


