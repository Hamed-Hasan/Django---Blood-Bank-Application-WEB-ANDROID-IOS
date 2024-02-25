from rest_framework import generics, permissions
from .models import DonationHistory
from .serializers import DonationHistorySerializer
from django.db.models import Q
from rest_framework import filters

class DonationHistoryListAPIView(generics.ListAPIView):
    serializer_class = DonationHistorySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['donor__username', 'recipient__username', 'event__title', 'status']

    def get_queryset(self):
        user = self.request.user
        return DonationHistory.objects.filter(Q(donor=user) | Q(recipient=user))


        # return DonationHistory.objects.all()


