from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import UserSignupForm, UserLoginForm

from django.contrib import messages
# Create your views here.


def login_user(request): 
    if request.user.is_authenticated:
        return redirect("home")    

    if request.method == "POST":
        form = UserLoginForm(request.POST)

        if form.is_valid():
            
            cd = form.cleaned_data
            user = authenticate(request,
                username = cd["username"],
                password = cd["password"],
                )
    
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcom back, {user.username}")
                return redirect("home")                
            else :
                messages.error(request, "Invalid input")
        
        else:
            messages.error(request, "Inputs should not be empty")

    form = UserLoginForm()
    return render(request, "accounts/login-form.html" , {
        "form": form
    }) 


def logout_user(request):
    if request.user.is_authenticated:
        logout(request) 
    return redirect('login_user')



def user_signup(request):
    if request.method == "POST":
        
        form = UserSignupForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create(username = cd["username"], email = cd["email"], password = cd["password"])
            login(request, user)
            
            messages.success(request, f"Dear {user.username} Welcom to my first Django Project")
            return redirect("home")

    elif request.user.is_authenticated:
        return redirect("home")
        

    form = UserSignupForm()
    return render(request , "accounts/signup-form.html", {
        "form" : form
    })