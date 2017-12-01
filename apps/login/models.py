from __future__ import unicode_literals
from django.db import models
import re, bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+$')
# Create your models here.
class UserManager(models.Manager):
	def register(self, data):
		error= []
		for field in data:
			if not EMAIL_REGEX.match(data['email']):
				error.append(field+"email not valid.")
			if len(data['first_name'])<2:
				error.append("First name can not be less then 2 characters long.")
			if len(data['last_name'])<2:
				error.append("Last name can not be less then 2 characters long.")
			try:
				self.get(email=data['email'])
				error.append("Email already exist.")
			except:
				pass
			if not NAME_REGEX.match(data['first_name']) or not NAME_REGEX.match(data['last_name']):
				error.append("Name must be letters.")
			if len(data['pass'])<8:
				error.append("Email must be more than 8 letters.")
			if not data['pass']==data['cpass']:
				error.append("Password does not match.")
			if len(error) != 0:
				return {'error':error}
			data['pass'] = bcrypt.hashpw(data['pass'].encode('utf8'), bcrypt.gensalt())
			user = self.create(first_name=data['first_name'], last_name=data['last_name'], email=data['email'], password=data['pass'])
			return {'user': user}
	def login(self, data):
		error=[]
		if len(data['email'])<2:
				error.append("Email can not be empty.")
		try:
			user=self.get(email=data['email'])
			if bcrypt.hashpw(data['pass'].encode('utf8'), user.password.encode('utf8'))== user.password.encode('utf8'):
				return {'user':user}
			error.append("Password does not match.")
		except:
			error.append("Email is not registered.")
		return {'error':error}



class User(models.Model):
	first_name=models.CharField(max_length=45)
	last_name=models.CharField(max_length=45)
	email=models.EmailField()
	password=models.CharField(max_length=100)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	objects = UserManager()
