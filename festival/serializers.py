from rest_framework import serializers
from .models import *

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields=('id','post','contents','created')    

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        # 유저를 기존에 넣어뒀는데 그러는 거 아님 
        # 그렇게 하면 내 계정으로 작성이 아닌 유저를 낵 ㅏ선택하게 되는 이상한 ...
        fields=('id','title', 'school', 'contents', 'created', 'comments')
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields=('id', 'info', 'created', 'contents')

class InfoSerializer(serializers.ModelSerializer):
    info_reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Info
        fields=('id', 'school','region','start_date','end_date','fes_location','lineup','created','info_reviews')