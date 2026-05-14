from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    profile = models.ImageField(upload_to='user_images/', blank=True, null=True)
    nickname = models.CharField(max_length=50)
    myschool = models.CharField(max_length=50, blank=True, null=True)
    birth = models.DateField(blank=True, null=True)
    likearea = models.CharField(max_length=50, blank=True, null=True)
    likeschool = models.CharField(max_length=50, blank=True, null=True)
