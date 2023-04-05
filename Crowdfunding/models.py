from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Campaign(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    goal = models.DecimalField(max_digits=10, decimal_places=2)
    crypto_address = models.CharField(max_length=42)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='fundraiser_images/')

    def __str__(self):
        return self.title

class Pledge(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    backer = models.ForeignKey(User, on_delete=models.CASCADE)
