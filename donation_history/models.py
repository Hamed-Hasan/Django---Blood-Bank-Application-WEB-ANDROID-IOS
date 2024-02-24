from django.db import models
from django.conf import settings
from events.models import Event

class DonationHistory(models.Model):
    donor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='donated', on_delete=models.CASCADE)
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='received', on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=[('donated', 'Donated'), ('canceled', 'Canceled')])

    def __str__(self):
        return f"{self.donor.username} -> {self.recipient.username}"
