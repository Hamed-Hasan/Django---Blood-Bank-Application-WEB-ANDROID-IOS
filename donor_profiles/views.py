from django.shortcuts import render

from rest_framework import generics, permissions
from .models import DonorProfile
from .serializers import DonorProfileSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class AvailableDonorListView(generics.ListAPIView):
    queryset = DonorProfile.objects.filter(availability=True)
    serializer_class = DonorProfileSerializer
    permission_classes = []  # No permission required as it's a public list

class DonorProfileUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = DonorProfile.objects.all()
    serializer_class = DonorProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        profile, created = DonorProfile.objects.get_or_create(
            user=self.request.user,
            defaults={
                'age': 0, 
                'address': '',  # Default address
                'availability': True,  # Default availability
                'blood_group': 'O+',  # Default blood group ( can change this to any valid choice)
                # 'identification_document': None,  # Default identification document (not needed because the field allows null)
                # 'last_donation_date': None,  # Default last donation date (not needed because the field allows null)
            }
        )
        return profile


