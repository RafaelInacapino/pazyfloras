from django.http import HttpResponse
from django.shortcuts import redirect

def login_required(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            print("AUTENTICADO y NO SUPERUSER") 
            return view_func(request, *args, **kwargs)
        print("NO AUTENTICADO")
        return redirect('/tienda/cuenta/login')       
    return wrapper_func

def superuser_required(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_superuser:
            print("AUTENTICADO y SUPERUSER") 
            return view_func(request, *args, **kwargs)
        if request.user.is_authenticated:
            print("AUTENTICADO y NO SUPERUSER") 
            return redirect('/accesodenegado')   
        print("NO AUTENTICADO")    
        return redirect('/accesodenegado')   
    return wrapper_func