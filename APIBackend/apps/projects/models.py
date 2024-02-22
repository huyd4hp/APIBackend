from django.db import models
from apps.users.models import CustomUser
# Create your models here.

STATUS_CHOICES = (
    ('InProcess', 'Đang tiến hành'),
    ('Done', 'Hoàn thành'),
)
class Project(models.Model):
    name = models.CharField(max_length = 50,null = True,blank=True)
    status = models.CharField(max_length= 10,choices = STATUS_CHOICES, default = 'InProcess')
    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length = 50,null = True,blank=True)
    assigned_to = models.ForeignKey(CustomUser,on_delete = models.SET_NULL, null=True,blank=True)
    project = models.ForeignKey(Project,on_delete=models.CASCADE, null=True,blank=True)
    status = models.CharField(max_length= 10,choices = STATUS_CHOICES, default = 'InProcess')
    created_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.name
    
