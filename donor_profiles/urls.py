from django.urls import path
from .views import DonorProfileUpdateAPIView, AvailableDonorListView

urlpatterns = [
    path('profile/', DonorProfileUpdateAPIView.as_view(), name='donor_profile_update'),
    path('available-donors/', AvailableDonorListView.as_view(), name='available_donors_list'),
]
