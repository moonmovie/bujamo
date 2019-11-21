from django.shortcuts import render
from accounts.models import User
from django.contrib import auth
from django.contrib import messages
from django.http import HttpResponse
# from .models import User
# Create your views here.

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'signup.html')
        else :
            return render(request, 'login.html')
    else:
        return messages.add_message(request,messages.INFO, 'Success')

def signup(request):
    if request.method=="POST":
        if request.POST["password1"] == request.POST["password2"]:
            User.objects.create_user(
                username=request.POST["username"],
                password=request.POST["password1"],
                email=request.POST["email"]
            )
        else:
            return render(request, 'signup.html',{'error' : '패스워드가 일치하지 않습니다.'})
            # auth.login(request,user)
            return render(request, 'login.html')
        return render(request, 'signup.html')
    return render(request, 'signup.html')