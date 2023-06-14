from rest_framework import serializers
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from home.models import *
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

class resetPasswordSerializer(serializers.Serializer):
        email=serializers.EmailField()
        otp=serializers.CharField()
        resetToken=serializers.CharField()
        password=serializers.CharField()
        confirmPassword=serializers.CharField()

        def validate(self, data):
            if data['password']!=data['confirmPassword']:
                raise serializers.ValidationError('Password and confirm password not matched')

            if not len(data['password'])>7:
                raise serializers.ValidationError('Password length should be greater than or equal to 8')
            return data
        
class userSupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_support
        fields='__all__'
    # user_id=serializers.IntegerField()
    # issue_message=serializers.TextField()
    # image=serializers.ImageField()

class userAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = userAddress
        fields='__all__'
        # fields=['user_id','image','issue_message']

class sellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = seller
        fields='__all__'

class sellerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = sellerAddress
        fields='__all__'

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields='__all__'

class productImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = productImages
        fields='__all__'

class cartSerializer(serializers.ModelSerializer):
    class Meta:
        model = cart
        fields='__all__'

class wishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = wishlist
        fields='__all__'

class productReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = productReview
        fields='__all__'

class ordersSerializer(serializers.ModelSerializer):
    class Meta:
        model = orders
        fields='__all__'

class productQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = productQuestions
        fields='__all__'