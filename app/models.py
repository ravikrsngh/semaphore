from django.db import models
from django.contrib.auth.models import AbstractUser, User
# Create your models here.
class marketer(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	noreg=models.BigIntegerField(blank=True,null=True)
	total_amount=models.BigIntegerField(blank=True,null=True)
	income=models.BigIntegerField(blank=True,null=True)
	boss=models.BooleanField(default=False)
	undercover=models.BooleanField(default=False)
	t_reg=models.BigIntegerField(blank=True,null=True)
	t_amount=models.BigIntegerField(blank=True,null=True)

	def __str__(self):
		return self.user.first_name

class eventssss(models.Model):
	name=models.CharField(max_length=200,blank=True,null=True)

	def __str__(self):
		return self.name

class userprofile(models.Model):
	"""docstring for userprofile."""
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	phone=models.CharField(max_length=10,blank=True,null=True)
	sem=models.CharField(max_length=10,blank=True,null=True)
	usn=models.CharField(max_length=50,blank=True,null=True)
	branch=models.ForeignKey('Department',on_delete=models.CASCADE,null=True)
	person=models.CharField(max_length=50,blank=True,null=True)
	eve=models.ForeignKey('eventssss',on_delete=models.CASCADE,null=True)
	college=models.CharField(max_length=50,blank=True,null=True)

	def __str__(self):
		return self.user.first_name


class Department(models.Model):
	"""
	Description: Model Description
	"""
	name = models.CharField(max_length = 50,blank = True,null = True )

	def __str__(self):
		return self.name
