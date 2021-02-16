from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login

# Create your views here.


def signupfunc(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            User.objects.create_user(username, "", password)
            return render(request, "signup.html", {})
        except IntegrityError:
            return render(
                request, "signup.html", {"error": "This username is already taken."}
            )
    return render(request, "signup.html", {})


def loginfunc(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=username)
        if user is not None:
            login(request, user)
            redirect()


def listfunc(request):
    return render(request, "list.html", {})
