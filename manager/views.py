from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from . import forms
from .models import Talk

def index(request):
	all_talks = []
	empty = 1
	if(len(Talk.objects.all()) == 0):
		all_talks.append("No available Talk")
	else:
		all_talks = Talk.objects.order_by('-priority')
		empty = 0
	if(request.user.is_authenticated):return render(request, 'manager/index.html', context={'usrname': request.user.username, "all_talks": all_talks, "flag": empty})
	else: return render(request, 'manager/index.html', context={"all_talks": all_talks, "flag": empty})

def signup(request):
	if(request.method == 'POST'):
		form = forms.Signup(request.POST)
		if(form.is_valid()):
				user = User.objects.create_user(first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'], username=form.cleaned_data['usrname'], password=form.cleaned_data['psswd'], email=form.cleaned_data['email'])
				user.save()
				return redirect('manager:index')
	else:
		form = forms.Signup()
	return render(request, 'registration/signup.html', {'form': form})

def login_redirect(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	user = authenticate(username=username, password=password)
	if user is not None:
		login(request, user)
		return HttpResponseRedirect(reverse('manager:index'))
	else:
		return HttpResponse('Wrong Username or Password')

def addtalk(request):
	if(request.method == 'POST'):
		form = forms.Addtalk(request.POST)
		if(form.is_valid()):
			talk = Talk.objects.create(description=form.cleaned_data['description'], priority=-2, name=form.cleaned_data['name'], email=form.cleaned_data['email'])
			talk.save()
			return redirect('manager:index')
	else:
		form = forms.Addtalk()
	return render(request, 'manager/addtalk.html', {'form': form})
