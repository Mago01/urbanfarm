from django.contrib import admin

# Register your models here.
from .models import Goods, User, Cart
admin.site.register(User)
admin.site.register(Goods)
admin.site.register(Cart)