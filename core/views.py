from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from core.forms import *
from core.models import *

# Create your views here.

def home(request, color=None):
	polygons = Polygon.objects.all()

	colors = []
	for polygon in polygons:
		if not (polygon.color,polygon.color[1:]) in colors:
			colors+=[(polygon.color,polygon.color[1:])]
	
	if color is not None:
		polygons = Polygon.objects.filter(color__icontains=color)

	try:
		if request.session['error']:
			error = request.session['error']
			del request.session['error']
		else:
			error = ""
	except:
		error = ""

	quarries = Quarry.objects.all()
	return render(request, 'home.html', {'polygons':polygons, 'colors':colors, 'quarries':quarries,'error':error})


@login_required
def save_map(request, map_id=None):
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
	Polygon.objects.get(id=map_id).delete()
	return redirect('/')


@login_required
def edit_map(request, map_id):
	polygons = Polygon.objects.all()
	colors = []
	for polygon in polygons:
		if not (polygon.color,polygon.color[1:]) in colors:
			colors+=[(polygon.color,polygon.color[1:])]

	polygon = Polygon.objects.get(id=map_id)

	quarries = Quarry.objects.all()
	return render(request, 'home.html', {'polygons':polygons, 'colors':colors, 'quarries':quarries, 'edit':map_id, 'polygon':polygon})


@login_required
def add_quarry(request, map_id):
	polygons = Polygon.objects.all()
	colors = []
	for polygon in polygons:
		if not (polygon.color,polygon.color[1:]) in colors:
			colors+=[(polygon.color,polygon.color[1:])]

	polygon = Polygon.objects.get(id=map_id)

	if request.method == 'POST':
		form = QuarryForm(request.POST)
		if form.is_valid():
			quarry = form.save()
			polygon.prices.add(quarry)
			polygon.save()
			return redirect('/')
	else:
		form = QuarryForm()

	quarries = Quarry.objects.all()
	return render(request, 'home.html', {'polygons':polygons, 'colors':colors, 'quarries':quarries, 'add_quarry':map_id, 'polygon':polygon, 'form':form})



def login_aux(request):
	if request.method == "POST":
	    username = request.POST['username']
	    password = request.POST['password']
	    user = authenticate(username=username, password=password)
	    if user is not None:
	      if user.is_active:
	        login(request, user)
	    else:
	    	request.session['error'] = "Invalid username/password"
	return redirect('/')


def logout_aux(request):
	logout(request)
	return redirect('/')


