from django.urls import path
from .views import DonorProfileUpdateAPIView

urlpatterns = [
    path('profile/', DonorProfileUpdateAPIView.as_view(), name='donor_profile_update'),
]
