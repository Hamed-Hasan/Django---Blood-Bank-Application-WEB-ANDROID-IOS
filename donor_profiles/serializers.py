from rest_framework import serializers
from .models import DonorProfile

class DonorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonorProfile
        fields = ['user', 'age', 'address', 'blood_group', 'last_donation_date', 'availability', 'identification_document']
        extra_kwargs = {
            'user': {'read_only': True},
            'last_donation_date': {'required': False},
            'identification_document': {'required': False},
        }

    def validate_age(self, value):
        if value < 18:
            raise serializers.ValidationError("Donors must be at least 18 years old.")
        return value

    def validate_blood_group(self, value):
        valid_blood_groups = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
        if value not in valid_blood_groups:
            raise serializers.ValidationError("This is not a valid blood group.")
        return value
