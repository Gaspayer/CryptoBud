from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class CreatorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    website = models.URLField()
    avatar = models.ImageField()

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    creator = models.ForeignKey(CreatorProfile, on_delete=models.CASCADE)
