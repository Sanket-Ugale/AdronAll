from rest_framework import serializers
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User=get_user_model()
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['email','password']

    def create(self,validated_data):
        user=User.objects.create(email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class verifyOTPSerializer(serializers.Serializer):
        email=serializers.EmailField()
        otp=serializers.CharField()

class forgotPasswordSerializer(serializers.Serializer):
        email=serializers.EmailField()
