from django.db import models

from django.contrib.auth.models import User


class UserProfile(models.Model):
        
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('X', 'X'),
    )
    NOTIFICATIONS = (
        ('P', 'Push'),
        ('S', 'SMS'),
        ('E', 'Email'),
        ('N', 'Non')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.CharField(max_length=140)
    bio = models.CharField(max_length=500)
    phone = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDERS, default='X')
    private = models.BooleanField()
    sugest = models.BooleanField(default=True)
    image = models.ImageField(upload_to='profilepics', blank=True, default='default.png')
    notification = models.CharField(max_length=1, choices=NOTIFICATIONS, default='P')

    def __str__(self):
        return self.user.username