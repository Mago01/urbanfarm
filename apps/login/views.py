from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
def index (request):
	return render(request, 'login/index.html')
def login (request):
	result = User.objects.login(request.POST.copy())
	if 'error'in result:
		for error in result['error']:
			messages.add_message(request, messages.ERROR, error)
		return redirect('/')
	request.session['user']=result['user'].first_name
	request.session['user_id']=result['user'].id
	return redirect('/done')
def register(request):
	result = User.objects.register(request.POST.copy())
	if 'error'in result:
		for error in result['error']:
			messages.add_message(request, messages.ERROR, error)
		return redirect('/')
	request.session['user']=result['user'].first_name
	request.session['user_id']=result['user'].id
	return redirect('/done')
def logout (request):
	request.session.clear()
	return redirect('/')
def done(request):
	return render(request,'login/welcome.html')
def edit(request, id):
 	y=Product.objects.get(id=id)
 	context={
    "product":y,
    }
	request.session['id']=id
	return render(request,'login/update.html', context)
def update(request):
	result = User.objects.register(request.POST.copy())
	if 'error'in result:
		for error in result['error']:
			messages.add_message(request, messages.ERROR, error)
		return redirect('/update.html')
	request.session['user']=result['user'].first_name
	request.session['user_id']=result['user'].id
	return redirect('/done')


