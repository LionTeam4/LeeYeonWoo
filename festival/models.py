from django.db import models

# 대학교마다 축제 정보 = Festival_info
# 지역,학교,일정(날짜,시간),장소,라인업(학교의 어디에 있는지)
# 지역,학교,날짜 -> 필터링
class Info (models.Model):
    school = models.CharField(max_length=50)
    image = models.ImageField(upload_to='festival_images/', blank=True, null=True)
    region = models.CharField(max_length=50)
    date = models.DateField()
    fes_location = models.CharField(max_length=50)
    lineup = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.school
    
# 후기 커뮤니티 = Review
# 사용자들 후기글, 사진 블로그처럼
class Review (models.Model):
    school = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=500)
    
    def __str__(self):
        return self.school, self.title