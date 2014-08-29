from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Response(models.Model):
	# response_one = models.CharField(max_length = 200)
	# response_two = models.CharField(max_length = 200)
	# response_three= models.CharField(max_length = 200)
	
	# def __str__(self):
		# return self.response_one

class questions(models.Model):
	code = models.SlugField(max_length = 10)
	q_1 = models.CharField(max_length = 100)
	q_2 = models.CharField(max_length = 100)
	q_3 = models.CharField(max_length = 100)
	created = models.DateTimeField(auto_now_add=True)
	
	people = models.Manager()
	
	def __str__(self):
		return self.q_1
	
		
class UserProfile(models.Model):
	user = models.OneToOneField(User, help_text = "")
	website = models.URLField(blank = True)
	
	def __unicode__(self):
		return self.user.username
