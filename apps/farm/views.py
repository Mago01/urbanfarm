from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Farm
from ..login.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django import forms
from .forms import FarmImage
from django.template import RequestContext
from django.core.files.storage import FileSystemStorage
from django.conf import settings

def farm (request):
	id = request.session['user_id']
	context = {
		"my_farm": Farm.objects.filter(seller__id=id)
	}

	return render(request, 'farm/farm.html', context)

def add (request):
    return render(request, 'farm/add.html')

def create (request):
	print '*'*80
	print request.FILES
	if len(request.POST['name']) < 1:
		messages.add_message(request, messages.WARNING, "Item name cannot be blank.")
		return redirect('/farm/add')
	if len(request.POST['description']) < 15:
		messages.add_message(request, messages.WARNING, "Description must be more than 15 characters.")
		return redirect('/farm/add')

	if request.method == 'POST':
		form = FarmImage(request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/home')
	else:
		form = FarmImage()

	x = User.objects.get(id=request.session['user_id'])
	print request.FILES
	newimage = request.FILES['image']
	newproduct = Farm.objects.create(name=request.POST['name'], description=request.POST['description'], type_food=request.POST['type_food'], unit=request.POST['unit'], price=request.POST['price'], image = newimage, seller = x, sold_in=request.POST['sold_in'])

	return redirect('/farm', {
        'form': form
    }
	)

def shop(request):
	if not 'user' in request.session:
		return redirect('/')

	id = request.session['user_id']
	farm_list = Farm.objects.exclude(seller__id=id)
	page = request.GET.get('page', 1)
	paginator = Paginator(farm_list, 4)

	try:
		items = paginator.page(page)
	except PageNotAnInteger:
		items = paginator.page(1)
	except EmptyPage:
		items = paginator.page(paginator.num_pages)

	return render(request, 'farm/saleitems.html', { 'items' : items})

def item(request, id):
	data = {
	    "products" : Farm.objects.filter(id=id)
	}

	return render(request, 'farm/item.html', data)
