from django.shortcuts import render, redirect
from .models import *


from django.http import FileResponse
from PROYECTO3.forms import FileForm, FileFormSignUp, FileForm2, FileFormRecursos, FileFormCategorias, FileFormClientes, FileFormFacturacion
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
        'title': 'Home'
    }

    try:
        response = requests.get(endpoint + 'buscardatos')
        buscardatos = response.json()

        context['datos'] = buscardatos

    except:
        print("API no esta corriendo")

    return render(request, "index.html", context=context)


def cargarXML1(request):
    ctx = {
        'content': None,
        'response': None
    }
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            f = request.FILES['file']
            xml_binary = f.read()
            xml = xml_binary.decode('utf-8')
            ctx['content'] = xml
            response = requests.post(endpoint + 'add', data=xml)
            messages.success(request, "XML CARGADO CORRECTAMENTE")
            if response.ok:
                response = requests.get(endpoint + 'buscarlistarecursos')

                buscarmsg = response.json()
                ctx['response'] = buscarmsg

            else:
                ctx['response'] = 'El archivo se envio, pero hubo un error en el servidor'
        else:
            messages.error(request, "EL XML NO FUE CARGADO CORRECTAMENTE")
    else:
        return render(request, 'cargarXML1.html')
    return render(request, 'cargarXML1.html', ctx)


def cargarXML2(request):
    ctx = {
        'content': None,
        'response': None
    }
    if request.method == 'POST':
        form = FileForm2(request.POST, request.FILES)
        if form.is_valid():
            f = request.FILES['file2']
            xml_binary = f.read()
            xml = xml_binary.decode('utf-8')
            ctx['content'] = xml
            response = requests.post(endpoint + 'add2', data=xml)
            messages.success(request, "XML CARGADO CORRECTAMENTE")
            if response.ok:
                response = requests.get(endpoint + 'buscarlistaConsumos')

                buscarmsg = response.json()
                ctx['response'] = buscarmsg

            else:
                ctx['response'] = 'El archivo se envio, pero hubo un error en el servidor'
        else:
            messages.error(request, "EL XML NO FUE CARGADO CORRECTAMENTE")
    else:
        return render(request, 'cargarXML2.html')
    return render(request, 'cargarXML2.html', ctx)


def ayuda(request):
    context = {
        'datos': [],
        'title': 'Home'
    }

    try:
        response = requests.get(endpoint + 'buscardatos')
        buscardatos = response.json()

        context['datos'] = buscardatos

    except:
        print("API no esta corriendo")

    return render(request, "ayuda.html", context=context)


def pdf_view(request):
    pdf = open(PDF_FILES_FOLDER + 'ensayo.pdf', 'rb')
    return FileResponse(pdf)


def signUp(request):

    ctx = {
        'nombres': None,
        'apellidos': None,
        'correo': None,
        'contraseña': None
    }

    if request.method == 'POST':
        form = FileFormSignUp(request.POST, request.FILES)
        if form.is_valid():
            """response = requests.get(endpoint + 'buscarUsuario')
            datos= response.json()

            for x in datos:
                print (x)"""

            parametros = {
                'nombres': request.POST['nombres'],
                'apellidos': request.POST['apellidos'],
                'username': request.POST['username'],
                'correo': request.POST['correo'],
                'contraseña': request.POST['contraseña']

            }
            response = requests.post(endpoint+'crearUsuario', json=parametros)

            messages.success(request, "Usuario creado Correctamente")

            datos = response.text

            print(parametros)
            """ctx['nombre']= nombres
                ctx['apellidos']= apellidos
                ctx['correo']= correo
                ctx['contraseña']= contraseña"""

            response = requests.post(endpoint + 'crearUsuario', parametros)

        else:
            messages.error(
                request, "Hubo un problema al crear usuario, revise la informacion ingresada")

    return render(request, 'signUp.html', ctx)


def login(request):
    context = {
        'datos': [],
        'title': 'Home'
    }
    try:
        response = requests.get(endpoint + 'buscardatos')
        buscardatos = response.json()

        context['datos'] = buscardatos

    except:
        print("API no esta corriendo")

    return render(request, "login.html", context=context)


def buscarUsuarios(request):
    response = requests.get(endpoint + 'buscarUsuario')
    buscardatos = response.json()

    context['datos'] = buscardatos


def home(request):
    context = {
        'datos': [],
        'title': 'Home'
    }
    return render(request, "home.html", context=context)


def operaciones(request):
    return render(request, "operaciones.html")


def creardatos(request):
    return render(request, "creardatos.html")


def CrearRecursos(request):
    ctx = {
        "idRecurso": None,
        "nombre": None,
        "abreviatura": None,
        "metrica": None,
        "tipo": None,
        "valorxhora": None

    }
    if request.method == 'POST':
        form = FileFormRecursos(request.POST, request.FILES)
        if form.is_valid():
            parametros = {
                "idRecurso": request.POST["idRecurso"],
                "nombre": request.POST["nombre"],
                "abreviatura": request.POST["abreviatura"],
                "metrica": request.POST["metrica"],
                "tipo": request.POST["tipo"],
                "valorxhora": request.POST["valorxhora"]

            }

            response = requests.post(endpoint+'crearRecursos', json=parametros)

            messages.success(request, "Datos enviados correctamente")
        else:
            messages.success(request, "Hubo un error!")
    return render(request, "CrearRecursos.html", ctx)


def CrearCategorias(request):
    ctx = {


    }
    if request.method == 'POST':
        form = FileFormCategorias(request.POST, request.FILES)
        if form.is_valid():
            parametros = {
                "idCategoria": request.POST["idCategoria"],
                "nombreCategoria": request.POST["nombreCategoria"],
                "descripcionCategoria": request.POST["descripcionCategoria"],
                "cargaTrabajo": request.POST["cargaTrabajo"],
                "idConfiguracion": request.POST["idConfiguracion"],
                "nombreConfiguracion": request.POST["nombreConfiguracion"],
                "descripcionConfiguracion": request.POST["descripcionConfiguracion"],
                "idRecursosConfiguracion": request.POST["idRecursosConfiguracion"],
                "cantidad": request.POST["cantidad"]

            }

            response = requests.post(
                endpoint+'crearCategoria', json=parametros)

            messages.success(request, "Datos enviados correctamente")
        else:
            messages.success(request, "Hubo un error!")
    return render(request, "CrearCategorias.html", ctx)


def CrearClientes(request):
    if request.method == 'POST':
        form = FileFormClientes(request.POST, request.FILES)
        if form.is_valid():
            parametros = {
                "nit": request.POST["nit"],
                "nombreCliente": request.POST["nombreCliente"],
                "usuario": request.POST["usuario"],
                "clave": request.POST["clave"],
                "direccion": request.POST["direccion"],
                "email": request.POST["email"],
                "idInstancia": request.POST["idInstancia"],
                "idConfiguracion": request.POST["idConfiguracion"],
                "nombreInstancia": request.POST["nombreInstancia"],
                "fechaInicio": request.POST["fechaInicio"],
                "estado": request.POST["estado"],
                "fechaFinal": request.POST["fechaFinal"]

            }

            response = requests.post(endpoint+'crearClientes', json=parametros)

            messages.success(request, "Datos enviados correctamente")
        else:
            messages.success(request, "Hubo un error!")
    return render(request, "CrearClientes.html")


def consultardatos(request):
    context = {
        'content': None,
        'response': None
    }
    context2 = {
        'content2': None,
        'response2': None
    }
    context3 = {
        'content3': None,
        'response3': None
    }
    try:
        response = requests.get(endpoint + 'buscarlistarecursos')
        buscardatos = response.json()

        response2 = requests.get(endpoint + 'buscarlistaCategorias')
        buscardatos2 = response2.json()

        response3 = requests.get(endpoint+'buscarlistaClientes')
        buscardatos3 = response3.json()

        context['content'] = buscardatos
        context2['content2'] = buscardatos2
        context3['content3'] = buscardatos3

    except:
        print("Error al buscar las listas")

    # {"context2":context2}

    return render(request, "consultardatos.html", {"context": context['content'], "context2": context2['content2'], "context3": context3['content3']})


def facturacion(request):
    context = {
        'content': None,
        'response': None
    }

    if request.method == 'POST':
        form = FileFormFacturacion(request.POST, request.FILES)
        if form.is_valid():

            fechaInicio= form.cleaned_data['fechaInicio'].strftime("%d/%m/%Y")
            fechaFinal= form.cleaned_data['fechaFinal'].strftime("%d/%m/%Y")
            fechaInicio= str(fechaInicio).replace("-", "/")
            fechaFinal= str(fechaFinal).replace("-", "/")

            parametros = {
                'fechaInicio': fechaInicio,
                'fechaFinal': fechaFinal,


            }
            response = requests.post(endpoint+'procesoFacturacion', json=parametros)
            messages.success(request, "Fechas mandadas correctamente")

            response = requests.get(endpoint + 'obtenerFactura')
            buscardatos = response.json()

            context['content'] = buscardatos

        else:
            messages.error(
                request, "Hubo un problema al mandar la fecha")

    return render(request, "facturacion.html", {"context": context['content']})

def facturado(request):
    """context = {
        'content': None,
        'response': None
    }
    try:
        response = requests.get(endpoint + 'obtenerFactura')
        buscardatos = response.json()

        context['content'] = buscardatos

    except:
        pass"""
    return render(request,"facturado.html")


def infoestudiante(request):
    return render(request, "infoestudiante.html")


def reset(request):

    try:
        response = requests.delete(endpoint + 'reset')
        print(response.json)
    except:
        print('NO SE HA BORRADO NADA!!')
    return render(request, 'CargarXML1.html')
