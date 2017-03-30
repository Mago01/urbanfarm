from __future__ import unicode_literals
from django.db import models
from ..login.models import User
import re, bcrypt, decimal


class Farm(models.Model):
	name = models.CharField(max_length=90)
	description = models.TextField(max_length=500)
	type_food = models.EmailField()
	unit = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	image = models.ImageField(upload_to='documents/', blank=True, null=True)
	price = models.DecimalField(max_digits=5, decimal_places = 2)
	seller = models.ForeignKey(User, related_name = 'all_sellers')
