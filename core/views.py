from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from core.forms import *
from core.models import *


FILTER_VALUES = {
	"Ancaster":"011993",
	"Barrie / Elmvale":"000000",
	"Bradford / Innisfil":"4f8f00",
	"Brampton":"945200",
	"Burlington":"0096ff",
	"Caledon":"d783ff",
	"Etobicoke / Rexdale":"ff2f92",
	"Halton Hills":"00fa92",
	"Hamilton":"ff7e79",
	"Lincoln":"009051",
	"Maple & Aurora":"941751",
	"Midland":"797979",
	"Mississauga":"942193",
	"New Tecumseth / Stayner":"009193",
	"Oakville / Milton":"ff9300",
	"Oneida":"929000",
	"Orangeville West":"ff2600",
	"Orillia":"7a81ff",
	"Rockwood":"76d6ff",
	"Toronto / North York":"008f00",
	"Vaughan / King City":"0433ff",
	"Waterdown":"fffb00",
	"Waterloo / Cambridge":"941100"
}


def home(request, filter_value=None):
	if not request.user.is_authenticated():
		return redirect('/login/')

	polygons = Polygon.objects.all()
	
	if filter_value is not None:
		polygons = Polygon.objects.filter(color__icontains=FILTER_VALUES[filter_value])

	try:
		if request.session['error']:
			error = request.session['error']
			del request.session['error']
		else:
			error = ""
	except:
		error = ""

	quarries = Quarry.objects.all()
	return render(request, 'home.html', {'polygons':polygons, 'filters':FILTER_VALUES, 'quarries':quarries, 'error':error})


@login_required
def save_map(request, map_id=None):
	if not request.user.is_superuser:
		return redirect('/')

	if request.method == 'POST':
		if map_id:
			instance = Polygon.objects.get(id=map_id)
		else:
			instance = None
		
		form = PolygonForm(request.POST, instance=instance)
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
	return render(request, 'home.html', {'polygons':polygons, 'filters':FILTER_VALUES, 'quarries':quarries, 'edit':map_id, 'polygon':polygon})


@login_required
def add_quarry(request, map_id):
	if not request.user.is_superuser:
		return redirect('/')

	polygons = Polygon.objects.all()
	polygon = Polygon.objects.get(id=map_id)
	quarries = Quarry.objects.all()

	if request.method == 'POST':
		form = QuarryForm(request.POST)
		if form.is_valid():
			quarry = form.save()
			polygon.prices.add(quarry)
			polygon.save()
			return redirect('/')
	else:
		form = QuarryForm()

	return render(request, 'home.html', {'polygons':polygons, 'filters':FILTER_VALUES, 'quarries':quarries, 'add_quarry':map_id, 'polygon':polygon, 'form':form})


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
	return render(request, 'home.html', {'polygons':polygons, 'filters':FILTER_VALUES, 'quarries':quarries, 'edit_quarry':polygon.id, 'polygon':polygon, 'form':form})


@login_required
def remove_quarry(request, quarry_id):
	if not request.user.is_superuser:
		return redirect('/')

	Price.objects.get(id=quarry_id).delete()
	return redirect('/')


def login_aux(request):
	error = None
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

	return render(request, 'login.html', {'error':error})


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
	return render(request, 'access_info.html', {'info':info, 'users':users})




