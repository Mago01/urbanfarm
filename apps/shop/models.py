from django.db import models
from apps.farm.models import Items

# Create your models here.
class Goods(models.Model):
	price = models.IntegerField()
	productName = models.TextField(max_length = 45)
	class Meta:
		db_table = "goods"
class CartQueryset(models.query.QuerySet):
	def multi(self):
		return self.filter(qty=2)
	def secondAll(self):
		return self.all()
class CartManager(models.Manager):
	def get_queryset(self):
		return CartQueryset(self.model, using=self._db)
	def multi(self):
		return self.get_queryset().multi()
	def secondAll(self):
		self.get_queryset().secondAll()
class DumQueryset(models.query.QuerySet):
	def active(self):
	# have each function return a QuerySet
		print "queryset custom"
		return self.filter(is_active=True)
	def featured(self):
	# have each function return a QuerySet
		return self.filter(is_featured=True)
class DumManager(models.Manager):
	def get_queryset(self):
		return DumQueryset(self.model, using=self._db)
	def active(self): #  create a custom method to filter for active products
		print "active in manager"
		return self.get_queryset().active(is_active=True)
	def featured(self): #  create a custom method to filter for featured products
		return self.get_queryset().filter(is_featured=True)
class Dum(models.Model): 
	objects = DumManager()
	name = models.CharField(max_length=60)
	description = models.TextField()
	is_active = models.BooleanField(default=False)
	is_featured = models.BooleanField(default=False)
	created_at = models.DateTimeField('Created At')
	def __str__(self):
		return self.name

class User(models.Model):
	name = models.TextField(max_length= 45)
	dummy = models.TextField(default = "")
	class Meta:
		db_table = "user"

class procItems(Items):
	class Meta:
		proxy = True
class Cart(models.Model):
	qty = models.IntegerField()
	items = models.ForeignKey(Items)
	user = models.ForeignKey(User, primary_key = False)
	objects = CartManager()
	class Meta:
		db_table = "cart"