from django.db import models
# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=1024, default="")
    
    assigned_student = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='assigned_student', blank=True, null=True)
    assigned_class = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='assigned_class', blank=True, null=True)
    assigned_mentor = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='assigned_mentor', blank=True, null=True)

    TYPE_ENUM = [
        ('DOC', 'Document'),
        ('COD', 'Code')
    ]
    STATUS_ENUM = [
        ('STD', 'Started'),
        ('WRK', 'Working'), 
        ('SUB', 'Submitted'),
        ('EVL', 'Evaluated')
    ]
    type = models.CharField(max_length=3, default="DOC", choices=TYPE_ENUM)
    status = models.CharField(max_length=3, default="STD", choices=STATUS_ENUM)
    grade = models.CharField(max_length=3, default="0.00", blank=True)

    github_link = models.CharField(max_length=1024, default="", blank=True)
