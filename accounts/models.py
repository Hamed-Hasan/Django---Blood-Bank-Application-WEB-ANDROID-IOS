from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.crypto import get_random_string

class User(AbstractUser):
    email_verified = models.BooleanField(default=False)
    verification_token = models.CharField(max_length=100, blank=True, null=True)

    def generate_verification_token(self):
        token = get_random_string(length=50)
        self.verification_token = token
        self.save()
        return token
