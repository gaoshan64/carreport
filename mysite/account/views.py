from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from .forms import LoginForm

# Create your views here.

def user_login(request):
    if request.method =="POST":
        login_form=LoginForm(request.POST)
        if login_form.is_valid():
            cd =login_form.cleaned_data
            user =authenticate(username=cd['username'],password=cd['password'])

            if user:
                login(request,user)
                return HttpResponse("success")
            else:
                return HttpResponse("FAIL")
        else:
            return HttpResponse("Invalid login")

    if request.method == "GET":
        user=request.user
        login_form = LoginForm()
        return render(request,"login.html",{"form":login_form},{"user":user})