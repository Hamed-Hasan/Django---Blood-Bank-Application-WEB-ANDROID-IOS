from rest_framework import serializers
from .models import DonationHistory

class DonationHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DonationHistory
        fields = '__all__'
