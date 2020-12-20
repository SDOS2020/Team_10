import uuid
from django.db import models
from users.models import User
# Create your models here.

class Class(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mentor', null=True, blank=True)
    mentees = models.TextField(default="{}")
    posts = models.TextField(default="{}")
    projects = models.TextField(default="{}")



class Post(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    post_text = models.TextField()
    comments = models.TextField()

class Comment(models.Model):
    parent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='parent', null=True, blank=True)
    by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='by', null=True, blank=True)
    comment_text = models.TextField(default="")
