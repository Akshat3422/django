from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth,messages


# Create your views here.

def index(request):
    return render(request,'index.html') # type: ignore


def counter(request):
    posts=[1,2,3,4,5,'tim','tom','john']
    return render(request,'counter.html',{'posts':posts})


def register(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        RepeatPassword=request.POST['RepeatPassword']

        if password==RepeatPassword:
            if User.objects.filter(email =email).exists():
                messages.info(request,"Email Already Used")
                return redirect('register')
            elif(User.objects.filter(username=username)).exists():
                messages.info(request,"Username Already Used")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')
            
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('register')
        
    else:
        return render(request,'register.html')
    


def login_user(request):
    username=request.POST['username']
    password=request.POST['password']

    user = auth.authenticate(request, username=username, password=password)

    if not user:
        messages.info(request,"Credentials Invalid")
        return redirect('/')

    else:
        auth.login(request,user)

    return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def post(request,pk):
    return render(request,'post.html',{'pk':pk})