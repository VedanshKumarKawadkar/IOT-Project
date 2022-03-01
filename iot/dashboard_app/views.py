import imp
import re
from tabnanny import check
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserSignupForm
from .models import UserDetails
import bcrypt

# Create your views here.

def dashboard(request):
    username = request.session["username"]
    email = request.session["email"]
    return render(request, "index.html")

def login(request):
    if(request.method == "POST"):
        email = request.POST.get('login_email')
        pwd = request.POST.get('login_password')
        check_email = UserDetails.objects.filter(email=email)
        if len(check_email)==0:
            return JsonResponse({"msg":"Email Not Found."})
        else:
            db_user = UserDetails.objects.get(email=email)
            check_pass = db_user.password
            print(pwd, "\n", check_pass)
            if pwd == check_pass:
                username = db_user.username
                print(username)
                request.session["email"] = email
                request.session["username"] = username
                return render(request, "index.html")
            else:
                
                return JsonResponse({"msg":"Incorrect Password."})


def signup(request):
    if request.user.is_authenticated:
        return redirect("")
    if request.method == "POST":
        email = request.POST.get('signup_email')
        pwd = request.POST.get('signup_password')
        pwd = str(pwd)
        username = request.POST.get('signup_username')
        re_pwd = request.POST.get('signup_password_confirm')
        print(username, pwd, email, re_pwd)

        check_email = UserDetails.objects.filter(email=email)
        print(check_email, len(check_email))
        check_un = UserDetails.objects.filter(username=username)
        if len(check_email)>0:
            return JsonResponse({"msg":"Email already present"})
        elif len(check_email)==0 and len(check_un)>0:
            return JsonResponse({"msg":"Username already present"})
        if len(check_email)==0 and len(check_un)==0:
            if pwd!=re_pwd:
                return JsonResponse({"msg":"Passwords are not same"})
            else:
                newuser = UserDetails(
                    username=username,
                    email=email,
                    password=pwd
                )

                newuser.save()

                return JsonResponse({"msg":"New User Created!!"})


def login_signup_page(request):
    return render(request, "login-signup.html")