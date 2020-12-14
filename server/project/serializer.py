from rest_framework import serializers
from .models import *


class ProjectSerializer(serializers.Serializer):
    class Meta:
        model = Project
        fields = ('name', 'assigned_student','assigned_class','assigned_mentor','type','status','grade','github_link',)


