from django.urls import path
from .views import DonationHistoryListAPIView

urlpatterns = [
    path('history/', DonationHistoryListAPIView.as_view(), name='donation_history_list'),
]
