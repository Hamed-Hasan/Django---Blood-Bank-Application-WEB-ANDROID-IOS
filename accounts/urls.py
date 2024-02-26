from django.urls import path
from .views import RegistrationAPIView, LoginAPIView, LogoutAPIView, EmailVerificationAPIView

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('verify-email/', EmailVerificationAPIView.as_view(), name='verify_email'),
]


