from django import forms
from .models import Post, Review, Comment

class Postform(forms.ModelForm):
    class Meta:
        model = Post
        # 유저를 기존에 넣어뒀는데 그러는 거 아님 
        # 그렇게 하면 내 계정으로 작성이 아닌 유저를 낵 ㅏ선택하게 되는 이상한 ...
        fields=['title', 'school', 'image', 'contents']

class Commentform(forms.ModelForm):
    class Meta:
        model = Comment
        fields=['contents']
        
class Reviewform(forms.ModelForm):
    class Meta:
        model = Review
        fields=['contents']