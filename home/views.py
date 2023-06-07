from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from home.emails import send_otp_via_email

from home.serializers import UserSerializer, forgotPasswordSerializer, verifyOTPSerializer
# from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
User=get_user_model()

# Create your views here.
@api_view(['POST'])
def login_api(request):
    try:
        data=request.data
        username=data.get('username')
        password=data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            # token, _ = Token.objects.get_or_create(user=user)
            refresh = RefreshToken.for_user(user)
            return Response({
            # "token":str(token_obj),
            # "payload":serializer.data,
            "message":"Data Saved",
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            },
            status=status.HTTP_302_FOUND)
            # return Response({
            #     'token':str(token)
            # },status=status.HTTP_200_OK)
        else:
            return Response({'message':'Invalid Credentials'},status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        print(e)
        return Response({'message':'Some thing went wrong'},status=status.HTTP_400_BAD_REQUEST)


class RegisterUser(APIView):
    def post(self, request):
        serializer=UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"message":"Some thing went wrong","error":serializer.errors},status=status.HTTP_403_FORBIDDEN)
        
        try:
            send_otp_via_email(serializer.data['email'])
        except:
            return Response({"message":"Some thing went wrong","error":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        user=User.objects.get(email=serializer.data['email'])
        # token_obj, _=Token.objects.get_or_create(user=user)
        refresh = RefreshToken.for_user(user)
        
        return Response({
            # "token":str(token_obj),
            "payload":serializer.data,
            "message":"OTP send on "+serializer.data['email']+" Successfully.",
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            },
            status=status.HTTP_302_FOUND)

class verifyOTP(APIView):
    def post(self,request):
        try:
            data=request.data
            serializer=verifyOTPSerializer(data=data)
            if serializer.is_valid():
                email=serializer.data['email']
                otp=serializer.data['otp']
                user=User.objects.filter(email=email)
                if not user.exists():
                    return Response({"message":"User not found"},status=status.HTTP_404_NOT_FOUND)
                if user[0].otp != otp:
                    return Response({"message":"Invalid OTP"},status=status.HTTP_400_BAD_REQUEST)
                if user.first().verification_status == "verified":
                    return Response({"message":"Account already verified"},status=status.HTTP_400_BAD_REQUEST)
                user=user.first()
                user.verification_status = "verified"
                user.save()
                return Response({"message":"Account verified Successfully"},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"ERROR":str(e)},status=status.HTTP_200_OK)    


class forgotPassword(APIView):
    def post(self, request):
        serializer=forgotPasswordSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"message":"Some thing went wrong","error":serializer.errors},status=status.HTTP_403_FORBIDDEN)
        email=serializer.data['email']
        user=User.objects.filter(email=email)
        if not user.exists():
            return Response({"message":"User not found"},status=status.HTTP_404_NOT_FOUND)
        try:    
            # send_otp_via_email(serializer.data['email'])
            pass
        except:
            return Response({"message":"Some thing went wrong","error":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        # serializer.save()
        user=user.first()
        user.verification_status = "resting"
        user.save()
        user=User.objects.get(email=serializer.data['email'])
        # token_obj, _=Token.objects.get_or_create(user=user)
        refresh = RefreshToken.for_user(user)
        
        return Response({
            # "token":str(token_obj),
            "payload":serializer.data,
            "message":"OTP send on "+serializer.data['email']+" Successfully.",
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            },
            status=status.HTTP_302_FOUND)      

# @api_view(['POST',"GET"])
class demoApi(APIView):
    # authentication_classes=[TokenAuthentication]
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request):
        return Response({"message":"GET request from demoApi"},status=status.HTTP_200_OK)
    def post(self,request):
        return Response({"message":"POST request from demoApi"},status=status.HTTP_200_OK)
    def put(self,request):
        return Response({"message":"PUT request from demoApi"},status=status.HTTP_200_OK)
    def delete(self,request):
        return Response({"message":"DELETE request from demoApi"},status=status.HTTP_200_OK)
    def patch(self,request):
        return Response({"message":"PATCH request from demoApi"},status=status.HTTP_200_OK)
