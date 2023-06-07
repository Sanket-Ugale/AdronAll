from django.core.mail import send_mail
import random
from django.conf import settings
from .models import User
from django.template import loader

def send_otp_via_email(email):
    # print("1")
    subject="AdronAll Account verification OTP."
    otp=random.randint(100000,999999)
    # print("OTP")
    # print(otp)
    # message=""""""



    html_message = loader.render_to_string('otpEmail.html',{'otp':otp})
    # message=f"OTP: {otp}"
    
    # print([email])
    # print(subject)
    # print(message)
    email_from=settings.EMAIL_HOST
    # print(email_from)message
    send_mail(subject,"", 'sanketbhikajiugale@outlook.com', [email], fail_silently=False,html_message=html_message)
    user_obj=User.objects.get(email=email)
    user_obj.otp=otp
    user_obj.save()
    # print("OTP SAVED")
    