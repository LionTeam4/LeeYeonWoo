from django.db import models
from django.conf import settings
from accounts.models import CustomUser

# 게시글 Post
class Post (models.Model):
    # 사용자 탈퇴 시 게시물은 사라지지 않고, 사용자는 null처리 (탈퇴한 회원입니다.)
    # AUTH_USER_MODEL : 현재 유저 모델 이름
    user = models.ForeignKey(CustomUser, related_name='posts', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=50)
    # 필터링 다중선택 가능 (ex.이화여대,건국대 선택시 관련 게시물 필터링 ㄱㄴ)
    school = models.CharField(max_length=50)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    contents = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    def summary(self):
        return self.contents[:50]
    
    def __str__(self):
        return self.title

# 댓글 (Post - Comment)
class Comment (models.Model):
    user = models.ForeignKey(CustomUser, related_name='user_comments', on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(Post, related_name='post_comments', on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    contents = models.TextField(max_length=500)
    
    def approve(self):
        self.save()

    def __str__(self):
        return self.post
     
# 대학교마다 축제 정보 Info
# 지역,학교,일정(날짜,시간),장소,라인업(학교의 어디에 있는지)
# 지역,학교,날짜 -> 필터링
class Info (models.Model):
    school = models.CharField(max_length=50)
    image = models.ImageField(upload_to='festival_images/', blank=True, null=True)
    poster = models.ImageField(upload_to='festival_images/poster/', blank=True, null=True)
    region = models.CharField(max_length=50)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    fes_location = models.CharField(max_length=50)
    lineup = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    # 즐겨찾기
    favorite_users = models.ManyToManyField(CustomUser, related_name='favorite_users', blank=True)
    
    def __str__(self):
        return self.school    
    
# 후기 Review
class Review (models.Model):
    user = models.ForeignKey(CustomUser, related_name='user_reviews', on_delete=models.SET_NULL, null=True)
    # 축제 정보가 없어질 때 리뷰는 사라지지 않고, 축제 정보는 null처리
    info = models.ForeignKey(Info, related_name='info_reviews', on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    contents = models.TextField(max_length=500)
    
    def approve(self):
        self.save()

    def __str__(self):
        return self.info.school