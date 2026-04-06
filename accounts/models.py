from django.db import models
from django.contrib.auth.models import AbstractUser

# 유저 User
# 기디 변경 사항에서 모델만 변경 완료
class CustomUser (AbstractUser):
    profile = models.ImageField(upload_to='user_images/', blank=True, null=True)
    nickname = models.CharField(max_length=50)
    myschool = models.CharField(max_length=50)
    birth = models.DateField()
    likearea = models.CharField(max_length=50)
    likeschool = models.CharField(max_length=50)

