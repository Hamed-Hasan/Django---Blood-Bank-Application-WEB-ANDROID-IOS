from rest_framework import generics, permissions
from .models import DonationHistory
from .serializers import DonationHistorySerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class DonationHistoryListAPIView(generics.ListAPIView):
    serializer_class = DonationHistorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # print(self.request.user)
        return DonationHistory.objects.filter(donor=self.request.user)
        # return DonationHistory.objects.all()


