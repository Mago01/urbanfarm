from __future__ import unicode_literals
from django.db import models
import re, bcrypt, decimal


class Farm(models.Model):
	name = models.CharField(max_length=90)
	description = models.TextField(max_length=500)
	type_food = models.EmailField()
	unit = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	price = models.DecimalField(max_digits=5, decimal_places = 2)
    # seller = models.ForeignKey(User, related_name = "sellers")

