from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Event, EventAcceptance
from donation_history.models import DonationHistory
from .serializers import EventSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class DonationRequestListView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Exclude the events created by the user to not show their own requests
        return Event.objects.exclude(creator=self.request.user)


class EventCreateAPIView(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class EventAcceptAPIView(generics.GenericAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        event = self.get_object()
        if event.creator == request.user:
            return Response({'message': 'You cannot accept your own event'}, status=status.HTTP_400_BAD_REQUEST)
        
        if EventAcceptance.objects.filter(event=event, user=request.user).exists():
            return Response({'message': 'You have already accepted this event'}, status=status.HTTP_400_BAD_REQUEST)
        
        EventAcceptance.objects.create(event=event, user=request.user)

        # Automatically create a DonationHistory record
        DonationHistory.objects.create(
            donor=request.user,
            recipient=event.creator,  # Assuming the event creator is the recipient
            event=event,
            status='donated'  # or 'pending' if you want to track when the donation is completed
        )
        
        return Response({'message': 'Event accepted and donation history recorded'}, status=status.HTTP_201_CREATED)



class EventDetailAPIView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        event = self.get_object()
        can_accept = event.creator != request.user and not EventAcceptance.objects.filter(event=event, user=request.user).exists()
        response.data['can_accept'] = can_accept
        return response
