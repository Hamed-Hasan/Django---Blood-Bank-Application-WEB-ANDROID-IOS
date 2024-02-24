from django.db import models
from django.conf import settings

class DonorProfile(models.Model):
    BLOOD_GROUP_CHOICES = [
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    address = models.CharField(max_length=255)
    last_donation_date = models.DateField(null=True, blank=True)
    availability = models.BooleanField(default=True)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
    identification_document = models.FileField(upload_to='identification_documents/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
