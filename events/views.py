from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Event, EventAcceptance
from .serializers import EventSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

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
        _, created = EventAcceptance.objects.get_or_create(event=event, user=request.user)
        if created:
            return Response({'message': 'Event accepted'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'You have already accepted this event'}, status=status.HTTP_400_BAD_REQUEST)
