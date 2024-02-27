from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class user_account(models.Model):
    user = models.OneToOneField(User, related_name='account',on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=12, decimal_places=2,default=0)

    def __str__(self) -> str:
        return f'{self.user.first_name}'
