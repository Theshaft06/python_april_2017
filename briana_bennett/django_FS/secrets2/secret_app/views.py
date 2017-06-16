from django.shortcuts import render, redirect
import bcrypt
from .models import *
from django.contrib import messages
from django.db.models import Count
from datetime import datetime
import pytz
utc = pytz.utc 


# Create your views here.
def current_user(request):
	return User.objects.get(id = request.session['user_id'])

def index(request):
	return render(request, 'secret_app/index.html')

def register(request):
	check = User.objects.validateUser(request.POST)
	if request.method != 'POST':
		return redirect('/')
	if check[0] == False:
		for error in check[1]:
			messages.add_message(request, messages.INFO, error, extra_tags="registration")
			return redirect('/')
	if check[0] == True:
		#has password
		hashed_pw = bcrypt.hashpw(request.POST.get('password').encode(), bcrypt.gensalt())

		#create user
	user = User.objects.create(
		first_name = request.POST.get('first_name'),
		last_name = request.POST.get('last_name'),
		email = request.POST.get('email'),
		password = hashed_pw,
	)

	#add user to session, logging them in
	request.session['user_id'] = user.id
	#route to success page
	return redirect('/secrets')

def login(request):
	#find user
	user = User.objects.filter(email = request.POST.get('email')).first()

	#Check user credentials
	#add them to session and log in or add error message and route to home page
	if user and bcrypt.checkpw(request.POST.get('password').encode(), user.password.encode()):
		request.session['user_id'] = user.id
		return redirect('/secrets')
	else: 
		messages.add_message(request, messages.INFO, 'invalid credentials', extra_tags="login")
		return redirect('/')
	return redirect('/secrets')

def home(request):
	context = {
		'current_user': current_user(request),

	}
	return render(request, 'secret_app/secrets.html', context)

def add_secret(request):
	secret = Secret.objects.create(
		content = request.POST.get('content'),
		user = current_user(request)
	)
	return redirect('/secrets')

def show_most_popular(request):

	context = {
		'user' : current_user(request),
		'secrets' : Secret.objects.select_related('user').all().order_by('like')[:5],
		'current_datetime' : datetime.now(tz=utc),

	}
	return render(request, 'secret_app/most_popular.html', context)

def add_like_homepage(request):
	return redirect('/secrets')

def add_like_popular_page(request, id):
	Secret.like.add('like')
	return redirect('/secrets/most_popular')


















