"""adronall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from home import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
# router=DefaultRouter()
# router.register(r'userSupport',views.userAddressViewSet,basename='userSupport')

urlpatterns = [
    # path('api/',include(router.urls)),
    
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path("chat/", include("home.urls")),
    # path("", views.index, name="index"),
    path("admin/", admin.site.urls),
    # LOGIN URL
    path("login/",views.login_api),
    path("register/",views.RegisterUser.as_view()),
    path("demoApi/",views.demoApi.as_view()),
    path("verifyOTP/",views.verifyOTP.as_view()),
    path("forgotPassword/",views.forgotPassword.as_view()), 
    path("resetPassword/",views.resetPassword.as_view()),
    path("scheduleMail/",views.schedule_mail),
    path("api/userSupport/",views.userSupportAPI.as_view()),
    path("api/userAddress/",views.userAddressAPI.as_view()),
    path("api/seller/",views.sellerAPI.as_view()),
    path("api/sellerAddress/",views.sellerAddressAPI.as_view()),
    path("api/product/",views.productAPI.as_view()),
    path("api/productImages/",views.productImagesAPI.as_view()),
    path("api/cart/",views.cartAPI.as_view()),
    path("api/wishlist/",views.wishlistAPI.as_view()),
    path("api/productReview/",views.productReviewAPI.as_view()),
    path("api/orders/",views.ordersAPI.as_view()),
    path("api/productQuestions/",views.productQuestionsAPI.as_view()),

    # path("api/getUserAddress/",views.get_userAddress)
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)