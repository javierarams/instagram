from django.db import models
from apps.register.models import UserProfile
# Create your models here.

class Follower(models.Model):
	#follower = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
	followers = models.ManyToManyField(UserProfile, symmetrical=False)