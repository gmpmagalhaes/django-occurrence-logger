from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import SignupView

urlpatterns = [
    path('auth/login', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('auth/signup', SignupView.as_view(), name="signup_user"),
    path('auth/refresh-token', TokenRefreshView.as_view(), name='token_refresh'),
]