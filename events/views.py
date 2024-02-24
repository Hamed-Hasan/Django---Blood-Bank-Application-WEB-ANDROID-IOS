from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Event
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
        # Add logic for event acceptance here
        # For example, you might want to create a record in a separate model that tracks event acceptances
        return Response({'message': 'Event accepted'}, status=status.HTTP_200_OK)
