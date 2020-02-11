from django.contrib import auth
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# from django.contrib.auth.models import authenticate, login, logout


# Create your views here.

def user_login(request):
    # context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            # context['error'] = 'Username or Password wrong'
            return HttpResponse('error')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('../../')


def dashboard(request):
    return render(request, 'dashboard.html')
