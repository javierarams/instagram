from django.db import models
# Create your models here.
class User(models.Model):
	nickname = models.CharField(max_length = 50, primary_key=True)
	name = models.CharField(max_length = 50)
	website = models.CharField(max_length = 140)
	bio = models.CharField(max_length = 500)
	phone = models.IntegerField()
	email = models.EmailField(max_length = 140)
	gender = models.CharField(max_length = 1)
	private = models.BooleanField()
	sugest = models.BooleanField()

