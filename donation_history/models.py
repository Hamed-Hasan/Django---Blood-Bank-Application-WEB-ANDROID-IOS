from django.db import models
from django.conf import settings
from events.models import Event

class DonationHistory(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('donated', 'Donated'),
        ('canceled', 'Canceled'),
    ]

    donor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='donated', on_delete=models.CASCADE)
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='received', on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.donor.username} -> {self.recipient.username}, {self.event.title} ({self.status})"
