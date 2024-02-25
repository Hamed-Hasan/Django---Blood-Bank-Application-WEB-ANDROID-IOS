from rest_framework import serializers
from .models import DonationHistory
from django.conf import settings
# class DonationHistorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DonationHistory
#         fields = '__all__'


class UserNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ('id', 'username')

class DonationHistorySerializer(serializers.ModelSerializer):
    donor = UserNestedSerializer(read_only=True)
    recipient = UserNestedSerializer(read_only=True)
    
    class Meta:
        model = DonationHistory
        fields = '__all__'
