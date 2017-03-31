from django.shortcuts import render, redirect
from apps.shop.models import Goods, User, Cart, procItems
from apps.farm.models import Items
from django.core import serializers
# Create your views here.
def index(request):
	request.session['id'] = 3
	cartCount = len(Cart.objects.filter(user = request.session['id']))
	products = Items.objects.all()
	contents = {
		'products': products,
		'count' : cartCount
	}
	prox = procItems.objects.all()
	print prox
	return render(request, 'shop/index.html', contents)
def add(request):
	print request.POST
	product = procItems.objects.get(id = request.POST['proId'])
	user = User.objects.get(id=request.session['id'])
	print " trying to check"
	checkCart = Cart.objects.filter(user = user).filter(items = product)
	if len(checkCart) > 0:
		checkCart[0].qty += int(request.POST['qty'])
		newCart = checkCart[0]
	else:
		newCart = Cart.objects.create(user = user, qty = request.POST['qty'], items = product)
	newCart.save()
	return redirect('/')
def cart(request):
	print request.session['id']
	print "cart"
	cart = Cart.objects.filter(user = request.session['id'])
	print len(cart)
	total = 0
	for item in cart:
		total+= item.items.price * item.qty
		print item.items.price
	contents = {
		'cart': cart,
		'total': total
	}
	return render(request, 'shop/cart.html', contents)
def delete(request, cart_id):
	print cart_id
	delCart = Cart.objects.get(id=cart_id)
	delCart.delete()
	return redirect('shop_cart')