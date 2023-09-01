from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import logout,login
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile
from .decorators import unauthenticated_user, allowed_users,admin_only




def home(request):
    return render(request,'index.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def index(request):
    return render(request,'user/index1.html')

@unauthenticated_user
def login_page(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect(index)
        else:
            return redirect(login_page)
    return render(request,'login1.html')

def register(request):
    if request.method=="POST":
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password
        )
        group=Group.objects.get(name='customer')
        user.groups.add(group)
        # Profile.objects.create(
        #     fullname=username
        # )
        user.save()
        
        # user.set_password(password)
        return redirect(login_page)
    return render(request,'register.html')


def logout_page(request):
    logout(request)
    return redirect(login_page)




@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def profile(request,id):
    user=request.user.profile
    print(user)
    context={"user":user}
    return render(request,'user/profile.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userform(request,id):
    user=request.user.profile
    if request.method=="POST":
        user1=request.user.profile
        # profile=Profile.objects.all()
        username=request.POST.get("username")
        fullname=request.POST.get("fullname")
        address=request.POST.get("address")
        cityname=request.POST.get("cityname")
        state=request.POST.get("state")
        # user.fullname=fullname
        user1.fullname=fullname
        user1.address=address
        user1.cityname=cityname
        user1.state=state
        user1.save()
        return redirect(index)
    context={'user':user}
    return render(request,'user/userform1.html',context)
