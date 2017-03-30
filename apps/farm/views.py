from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Farm
from ..user.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def farm (request, id):

	context = {
		"my_farm": Farm.objects.filter(id=id)
	}

	return render(request, 'farm/farm.html', context)
	
def add (request):

	return render(request, 'farm/add.html')

def create (request):

    if len(request.POST['name']) < 1:
        messages.add_message(request, messages.WARNING, "Item name cannot be blank.")
        return redirect('/farm/add')
    if len(request.POST['description']) < 15:
        messages.add_message(request, messages.WARNING, "Description must be more than 15 characters.")
        return redirect('/farm/add')

    x = User.objects.get(id=request.session['user_id'])
    Farm.objects.create(name=request.POST['name'], description=request.POST['description'], seller = x)

    return redirect('/farm')

def shop(request):
	if not 'user' in request.session:
    return redirect('/')

	id = request.session['user']
	farm_list = Farm.objects.exclude(id=id)
	page = request.GET.get('page', 1)
	paginator = Paginator(farm_list, 6)

	try:
		items = paginator.page(page)
	except PageNotAnInteger:
		items = paginator.page(1)
	except EmptyPage:
		items = paginator.page(paginator.num_pages)

	return render(request, 'farm/saleitems.html', { 'items' : items})
