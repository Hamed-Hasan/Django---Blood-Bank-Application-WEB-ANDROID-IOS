from django.contrib.auth import get_user_model, login, logout
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import UserSerializer
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings

User = get_user_model()


class RegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        token = user.generate_verification_token()
        verification_url = self.request.build_absolute_uri(reverse('verify_email')) + f"?token={token}"
        send_mail(
            'Verify your email',
            f'Please click the following link to verify your email: {verification_url}',
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )

class LoginAPIView(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.filter(username=username).first()
        if user and user.check_password(password):
            login(request, user)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

class LogoutAPIView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)

class EmailVerificationAPIView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        token = request.query_params.get('token')
        user = User.objects.filter(verification_token=token).first()
        if user:
            user.email_verified = True
            user.verification_token = None
            user.save()
            return Response({'message': 'Email verified successfully'}, status=status.HTTP_200_OK)
        return Response({'message': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
