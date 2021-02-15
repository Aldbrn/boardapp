from django.shortcuts import render
from django.contrib.auth.models import User
from django.db import IntegrityError

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
    