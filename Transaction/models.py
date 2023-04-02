from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    sender = models.ForeignKey(Wallet, related_name='sent_transactions', on_delete=models.CASCADE)
    receiver = models.ForeignKey(Wallet, related_name='received_transactions', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
