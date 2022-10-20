from django.shortcuts import render,redirect
from .models import *

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# Create your views here.

# Create your views here.
endpoint = 'http://127.0.0.1:4000/'
def home(request):
    context = {
        'datos': [],
        'title' : 'Home'
    }
    
    try:
        response =requests.get(endpoint + 'buscardatos')
        buscardatos = response.json()
        
        context['datos']= buscardatos
       
    except:
        print("API no esta corriendo")    

    return render(request, "index.html",context=context)

def signUp(request):
    
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        

        if form.is_valid():
            
            nombre= form.cleaned_data['nombres']
            apellido = form.cleaned_data['apellidos']
            username= form.cleaned_data['username']
            correo= form.cleaned_data['correo']
            contraseña= form.cleaned_data['contraseña']

            messages.success(request,f'usuario {username}creado')
            return redirect("index")
        
            

    else:
            form = UserCreationForm()
            
            
            

    context= {'form': form}  
    return render(request, 'signUp.html',context)  
        
        
        
        
    
    

def login(request):
    context = {
        'datos': [],
        'title' : 'Home'
    }
    try:
        response =requests.get(endpoint + 'buscardatos')
        buscardatos = response.json()
        
        context['datos']= buscardatos
       
    except:
        print("API no esta corriendo")    

    return render(request, "login.html",context=context)

def buscarUsuarios(request):
    response =requests.get(endpoint + 'buscarUsuario')
    buscardatos = response.json()
        
    context['datos']= buscardatos
