from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=(
            'id','username','password','nickname','profile','myschool','birth','likearea','likeschool'
        )
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            nickname=validated_data['nickname'],
            profile=validated_data['profile'],
            myschool=validated_data['myschool'],
            birth=validated_data['birth'],
            likearea=validated_data['likearea'],
            likeschool=validated_data['likeschool'],
        )
        user.set_password(self.validated_data['password'])
        user.save()

        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)

            if not user.check_password(password):
                raise serializers.ValidationError()
            else:
                token = RefreshToken.for_user(user)
                refresh = str(token)
                access = str(token.access_token)

                return{
                    'id':user.id,
                    'username':user.username,
                    'access':access,
                    'refresh':refresh
                }