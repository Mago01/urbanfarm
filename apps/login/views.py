from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
def index (request):

	if 'user' in request.session: #this section is to redirect if a user is already logged in
		return redirect('/home')
	return render(request, 'login/index.html')
def login (request):
	result = User.objects.login(request.POST.copy())
	if 'error'in result:
		for error in result['error']:
			messages.add_message(request, messages.ERROR, error)
		return redirect('/')
	request.session['user']=result['user'].first_name
	request.session['user_id']=result['user'].id
	return redirect('/home')
def register(request):
	result = User.objects.register(request.POST.copy())
	if 'error'in result:
		for error in result['error']:
			messages.add_message(request, messages.ERROR, error)
		return redirect('/')
	request.session['user']=result['user'].first_name
	request.session['user_id']=result['user'].id
	return redirect('/home')
def logout (request):
	request.session.clear()
	return redirect('/')
def home(request):
	return render(request,'login/inside.html')

