from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Response(models.Model):
	response_one = models.CharField(max_length = 200)
	response_two = models.CharField(max_length = 200)
	response_three= models.CharField(max_length = 200)
	
	def __str__(self):
		return self.name
		
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	website = models.URLField(blank = True)
	
	def __unicode__(self):
		return self.user.username
