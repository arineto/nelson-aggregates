from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from random import randint
from core.forms import *
from core.models import *


def home(request, filter_value=None):
	if not request.user.is_authenticated():
		return redirect('/login/')

	polygons = Polygon.objects.all()
	
	if filter_value is not None:
		polygons = filter_maps(filter_value)

	try:
		if request.session['error']:
			error = request.session['error']
			del request.session['error']
		else:
			error = ""
	except:
		error = ""

	quarries = Quarry.objects.all()
	pdfs = PDF.objects.all()
	areas = Area.objects.all()
	return render(request, 'home.html', {'polygons':polygons, 'filters':areas, 'quarries':quarries, 'pdfs':pdfs, 'error':error})


@login_required
def save_map(request, map_id=None):
	if not request.user.is_superuser:
		return redirect('/')

	if request.method == 'POST':
		if map_id:
			instance = Polygon.objects.get(id=map_id)
			form = PolygonEditForm(request.POST, instance=instance)
		else:
			form = PolygonForm(request.POST)

		if form.is_valid():
			form.save()
		else:
			request.session['error'] = "Fill every field"

	return redirect('/')


@login_required
def delete_map(request, map_id):
	if not request.user.is_superuser:
		return redirect('/')

	Polygon.objects.get(id=map_id).delete()
	return redirect('/')


@login_required
def edit_map(request, map_id):
	if not request.user.is_superuser:
		return redirect('/')

	polygons = Polygon.objects.all()
	polygon = Polygon.objects.get(id=map_id)
	quarries = Quarry.objects.all()
	pdfs = PDF.objects.all()
	areas = Area.objects.all()
	return render(request, 'home.html', {'polygons':polygons, 'filters':areas, 'quarries':quarries, 'pdfs':pdfs, 'edit':map_id, 'polygon':polygon})


@login_required
def add_quarry(request, map_id):
	if not request.user.is_superuser:
		return redirect('/')

	polygons = Polygon.objects.all()
	polygon = Polygon.objects.get(id=map_id)
	quarries = Quarry.objects.all()
	pdfs = PDF.objects.all()
	areas = Area.objects.all()

	if request.method == 'POST':
		form = QuarryForm(request.POST)
		if form.is_valid():
			quarry = form.save()
			polygon.prices.add(quarry)
			polygon.save()
			return redirect('/')
	else:
		form = QuarryForm()

	return render(request, 'home.html', {'polygons':polygons, 'filters':areas, 'quarries':quarries, 'pdfs':pdfs, 'add_quarry':map_id, 'polygon':polygon, 'form':form})


@login_required
def edit_quarry(request, quarry_id):
	if not request.user.is_superuser:
		return redirect('/')

	instance = Price.objects.get(id=quarry_id)
	if request.method == 'POST':
		form = QuarryForm(request.POST, instance=instance)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = QuarryForm(instance=instance)

	polygons = Polygon.objects.all()
	polygon = Polygon.objects.filter(prices=instance)[0]
	quarries = Quarry.objects.all()
	pdfs = PDF.objects.all()
	areas = Area.objects.all()
	return render(request, 'home.html', {'polygons':polygons, 'filters':areas, 'quarries':quarries, 'pdfs':pdfs, 'edit_quarry':polygon.id, 'polygon':polygon, 'form':form})


@login_required
def remove_quarry(request, quarry_id):
	if not request.user.is_superuser:
		return redirect('/')

	Price.objects.get(id=quarry_id).delete()
	return redirect('/')


def login_aux(request):
	error = None
	try:
		login_picture = LoginPicture.objects.all().order_by('-id')[0]
	except:
		login_picture = None
	if request.method == "POST":
	    username = request.POST['username']
	    password = request.POST['password']
	    user = authenticate(username=username, password=password)
	    if user is not None:
	      if user.is_active:
	        login(request, user)
	        AccessInfo.objects.create(user=user)
	        return redirect('/')
	      else:
	      	error = "Not active user"
	    else:
	    	error = "Invalid username/password"

	return render(request, 'login.html', {'error':error, 'login_picture':login_picture})


def logout_aux(request):
	logout(request)
	return redirect('/')


@login_required
def access_info(request, username=None):
	if not request.user.is_superuser:
		return redirect('/')

	if username:
		info = AccessInfo.objects.filter(user=User.objects.get(username=username)).order_by('-date')
	else:
		info = AccessInfo.objects.all().order_by('-date')

	users = User.objects.all()
	pdfs = PDF.objects.all()
	return render(request, 'access_info.html', {'access_info':True, 'info':info, 'users':users, 'pdfs':pdfs})


def forgot_password(request):
	answer = None
	try:
		login_picture = LoginPicture.objects.all().order_by('-id')[0]
	except:
		login_picture = None
	if request.method == "POST":
		email = request.POST.get("email")
		try:
			user = User.objects.get(email=email)
			new_password = randint(100000, 999999)
			message = "Hello, \nThis is an answer to password recovery. Please change your password for security reasons.\nNew Password: "+str(new_password)
			email = EmailMessage('Nelson Aggregate - Zonning', message, to=[email])
			email.send()
			user.set_password(new_password)
			user.save()
			answer = "The password was sent to you email."
		except:
			answer = "There are no accounts registered in this email."

	return render(request, 'login.html', {'forgot_password':True, 'answer':answer, 'login_picture':login_picture})


@login_required
def change_password(request):
	error = None
	polygons = Polygon.objects.all()
	quarries = Quarry.objects.all()
	pdfs = PDF.objects.all()
	areas = Area.objects.all()
	if request.method == 'POST':
		form = ChangePasswordForm(request.POST)
		if not request.user.check_password(request.POST.get('old_password')):
			error = "Wrong old password"
		else:
			if form.is_valid():
				request.user.set_password(request.POST.get('password1'))
				request.user.save()
				return redirect('/')
	else:
		form = ChangePasswordForm()
	return render(request, 'home.html', {'polygons':polygons, 'filters':areas, 'quarries':quarries, 'pdfs':pdfs, 'change_password':True, 'form':form, 'error':error})


def filter_maps(filter_value):
	quarries = Quarry.objects.filter(name=filter_value)
	if len(quarries)>0:
		prices = Price.objects.filter(quarry__in=quarries)
		polygons = Polygon.objects.filter(prices__in=prices)
	else:
		polygons = Polygon.objects.filter(color__icontains=Area.objects.get(color=filter_value).color)
	return polygons

