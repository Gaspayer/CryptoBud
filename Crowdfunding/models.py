from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Campaign(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    goal = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

class Pledge(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    backer = models.ForeignKey(User, on_delete=models.CASCADE)
