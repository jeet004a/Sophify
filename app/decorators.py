from django.http import HttpResponse
from django.shortcuts import redirect
from . import views


def unauthenticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home1')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func



def allowed_users(allowed_roles=[]):
    def decorators(view_func):
        def wrapper_func(request,*args,**kwargs):
            group=None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
                if group in allowed_roles:
                    
                    return view_func(request,*args,**kwargs)
                else:
                    return HttpResponse("Nikal laude")
        return wrapper_func
    return decorators

def admin_only(view_func):
    def wrapper_function(request,*args,**kwargs):
        group=None
        if request.user.groups.exists():
            group=request.user.groups.all()[0].name
        if group=='customer':
            return redirect('home1')
        if group=='admin':
            return view_func(request,*args,**kwargs)
    return wrapper_function