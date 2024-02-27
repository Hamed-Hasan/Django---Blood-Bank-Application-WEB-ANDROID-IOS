from django.db import models
from django.contrib.auth.models import User
from user_accounts.models import user_account

# Create your models here.
class transaction_model(models.Model):
    account = models.ForeignKey(user_account,related_name='transactions' ,on_delete=models.CASCADE)
    amount = models.DecimalField( max_digits=12, decimal_places=2)
    timestamp = models.DateField( auto_now_add=True)
    #add

    class Meta:
        ordering = ['timestamp']

