from django.db import models
from django.conf import settings

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    blood_group = models.CharField(max_length=3)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='created_events')

    def __str__(self):
        return self.title

class EventAcceptance(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='acceptances')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='accepted_events')
    accepted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} accepted {self.event.title}"
