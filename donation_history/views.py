from rest_framework import generics, permissions
from .models import DonationHistory
from .serializers import DonationHistorySerializer
from django.db.models import Q

class DonationHistoryListAPIView(generics.ListAPIView):
    serializer_class = DonationHistorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Get donations where the user is either the donor or the recipient
        user = self.request.user
        return DonationHistory.objects.filter(Q(donor=user) | Q(recipient=user))

        # return DonationHistory.objects.all()


