from django.shortcuts import render,redirect
from .models import *

from django.http import FileResponse
from PROYECTO3.forms import FileForm,FileFormSignUp,FileForm2
from FRONTEND.settings import PDF_FILES_FOLDER


from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template

from django.contrib.staticfiles import finders

import requests
import io


# Create your views here.

# Create your views here.
endpoint = 'http://127.0.0.1:4000/'
def index(request):
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

def cargarXML1(request):
    ctx = {
        'content':None,
        'response':None
    }
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            f = request.FILES['file']
            xml_binary = f.read()
            xml = xml_binary.decode('utf-8')
            ctx['content'] = xml
            response = requests.post(endpoint + 'add', data=xml)
            if response.ok:
                response =requests.get(endpoint + 'buscarlistarecursos')
                
                
                
                buscarmsg = response.json()
                ctx['response'] = buscarmsg
                
            else:
                ctx['response'] = 'El archivo se envio, pero hubo un error en el servidor'
    else:
        return render(request, 'cargarXML1.html')
    return render(request, 'cargarXML1.html', ctx)

def cargarXML2(request):
    ctx = {
        'content':None,
        'response':None
    }
    if request.method == 'POST':
        form = FileForm2(request.POST, request.FILES)
        if form.is_valid():
            f = request.FILES['file2']
            xml_binary = f.read()
            xml = xml_binary.decode('utf-8')
            ctx['content'] = xml
            response = requests.post(endpoint + 'add2', data=xml)
            if response.ok:
                response =requests.get(endpoint + 'buscarlistaConsumos')
                
                
                
                buscarmsg = response.json()
                ctx['response'] = buscarmsg
                
            else:
                ctx['response'] = 'El archivo se envio, pero hubo un error en el servidor'
    else:
        return render(request, 'cargarXML2.html')
    return render(request, 'cargarXML2.html', ctx)

def ayuda(request):
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

    return render(request, "ayuda.html",context=context)

def pdf_view(request): 
    pdf = open(PDF_FILES_FOLDER + 'ProgramaLaboratorioIPC2.pdf', 'rb')
    return FileResponse(pdf)




def signUp(request):
    ctx = {
        'nombres':None,
        'apellidos':None,
        'correo': None,
        'contraseña':None
    }
    
    
    if request.method == 'POST':
        form = FileFormSignUp(request.POST,request.FILES)
        if form.is_valid():
            parametros ={
                'nombres':request.POST['nombres'],
                'apellidos':request.POST['apellidos'],
                'username': request.POST['username'],
                'correo': request.POST['correo'],
                'contraseña':request.POST['contraseña']

            }
            response= requests.post(endpoint+'crearUsuario',json=parametros)
            datos= response.text
            
            
            print(parametros)
            """ctx['nombre']= nombres
            ctx['apellidos']= apellidos
            ctx['correo']= correo
            ctx['contraseña']= contraseña"""

            response = requests.post(endpoint + 'crearUsuario', parametros)
        
        
        

        
        
            

    
            
            
            

      
    return render(request, 'signUp.html',ctx)  
        
        
        
        
    
    

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


def home(request):
    context = {
        'datos': [],
        'title' : 'Home'
    }
    return render(request, "home.html",context=context)


def reset(request):
    
    try:
        response =requests.delete(endpoint + 'reset')
        print(response.json)
    except:
        print('NO SE HA BORRADO NADA!!')
    return render(request,'CargarXML1.html') 