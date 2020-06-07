from django.http import HttpResponse
from django.shortcuts import redirect
from .models import VehicleCompany

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('vendor')
        else:    
            return view_func(request, *args, **kwargs)
    
    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            #print('working', allowed_roles)
            group=None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
            if group in allowed_roles:  
                return view_func(request, *args, **kwargs)
            else:
                return redirect('/unauthorized/')
        return wrapper_func
    return decorator    


def active_users(allowed_user=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            statusinfo=VehicleCompany.objects.get(user_auth=request.user)
            print(statusinfo.account_status)
            if statusinfo.account_status in allowed_user:
                return view_func(request, *args, **kwargs)
            elif statusinfo.account_status == 'Pending':
                return redirect('/pending/')
            else:
                return redirect('/deactivated/')
        return wrapper_func
    return decorator