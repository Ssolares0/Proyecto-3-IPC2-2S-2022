from django.urls import path
from . import views
urlpatterns =[
    path('',views.index,name ='index'),
    path('signUp/',views.signUp,name='signUp'),
    path('login/',views.login,name='login'),
    path('home/',views.home,name='home'),
    path('operaciones/',views.operaciones,name='operaciones'),
    path('creardatos/',views.creardatos,name='creardatos'),
    path('CrearRecursos/',views.CrearRecursos,name='CrearRecursos'),
    path('CrearCategorias/',views.CrearCategorias,name="CrearCategorias"),
    path('cargarXML1/',views.cargarXML1,name='cargarXML1'),
    path('cargarXML2/',views.cargarXML2,name='cargarXML2'),
    path('ayuda/',views.ayuda,name='ayuda'),
    path('pdf/', views.pdf_view, name='pdf'),
    path('reset/', view=views.reset,name='reset'),
    path('buscarUsers/',views.buscarUsuarios,name='buscarUsuarios')

]