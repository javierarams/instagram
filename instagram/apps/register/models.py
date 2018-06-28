from django.db import models

from django.contrib.auth.models import User


class UserProfile(models.Model):
        
    GENDERS = (
        ('M', 'M'),
        ('F', 'F'),
        ('X', 'X'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50, unique=True)
    website = models.CharField(max_length=140)
    bio = models.CharField(max_length=500)
    phone = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDERS)
    private = models.BooleanField()
    sugest = models.BooleanField()
    pic = models.ImageField(upload_to='profilepics')
