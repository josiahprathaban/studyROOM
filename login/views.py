from django.contrib.auth import authenticate
from django.db import IntegrityError
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.http import HttpResponse


def index(request):
    return render(request, 'login/index.html')


def login(request):
    return render(request, 'login/login.html')


def signup(request):
    return render(request, 'login/signup.html')


def success(request):
    try:
        user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'],
                                        email=request.POST['email'], first_name=request.POST['firstname'],
                                        last_name=request.POST['lastname'])
        user.save()
        return render(request, 'login/signupsucess.html')
    except IntegrityError:
        return render(request, 'login/signup.html', {'error': True})


def logout_user(request):
    logout(request)
    return render(request, 'login/index.html')

