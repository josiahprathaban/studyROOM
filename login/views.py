from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return render(request, 'login/index.html')


def login(request):
    return render(request, 'login/login.html')


def signup(request):
    return render(request, 'login/signup.html')
