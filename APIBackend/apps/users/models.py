from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.db import models


ROLE_CHOICES = (
        ('staff', 'Nhân viên'),
        ('manager', 'Quản lý'),
    )

class CustomUserManager(BaseUserManager):
    def create_user(self,username,password,**extra_fields):
        if not username:
            raise ValueError('The username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,username,password=None,**extra_fields):
        extra_fields.setdefault('role','manager')
        extra_fields.setdefault('is_staff', True)   
        extra_fields.setdefault('is_superuser', True)   
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        if not username:
            raise ValueError("Username is required")
        return self.create_user(username,password,**extra_fields)
    
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='staff')
    REQUIRED_FIELDS = ['email','first_name','last_name']

    def __str__(self):
        return self.username