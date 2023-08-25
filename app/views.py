from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

@login_required(login_url="login")
def home(request):
    return render(request,'index.html')



def login_page(requset):
    if requset.method=="POST":
        username=requset.POST.get("username")
        password=requset.POST.get("password")
        user=authenticate(username=username,password=password)
        if user is not None:
            login(requset,user)
            return redirect(home)
        else:
            messages.info(requset,"Nikal Eha seh")
            return redirect(login_page)
    return render(requset,'login.html')


def register(request):
    if request.method=="POST":
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        user.set_password(password)
        user.save()
        return redirect(login_page)

    return render(request,'register.html')

@login_required(login_url="login")
def user(request):
    # user=User.objects.get(id=pk)
    context={"user":user}

    return render(request,'user.html',context) 