from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

from home.manager import UserManager

# Create your models here.
class User(AbstractUser):
    username=None
    email=models.EmailField(unique=True)
    gender=models.CharField(max_length=10,null=True)
    birthDate=models.DateField(default=timezone.now)
    age=models.IntegerField(default=18)
    phone_number= models.CharField(max_length=10,null=True)
    verification_status=models.CharField(max_length=20,default='pending')
    verification_slug=models.CharField(max_length=100,null=True)
    otp =models.CharField(max_length=6, null=True)

    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS=[]
    objects=UserManager()

