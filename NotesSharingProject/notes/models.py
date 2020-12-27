from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Signup(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	contact=models.CharField(max_len=10,null=True)
	branch=models.CharField(max_len=30)
	role=models.CharField(max_len=15)

	def _str_(self):
		return self.user.username

class Notes(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	uploadingdate=models.CharField(max_len=30)
	branch=models.CharField(max_len=30)
	subject=models.CharField(max_len=30)
	notesfile=models.FileField(null=True)
	filetype=models.CharField(max_len=30)
	description=models.CharField(max_len=200,null=True)
	status=models.CharField(max_len=15)
	


	def _str_(self):
		return self.signup.user.username+" "+self.status


