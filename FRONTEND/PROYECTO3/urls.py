from django.urls import path
from . import views
urlpatterns =[
    path('',views.home,name ='index'),
    path('signUp/',views.signUp,name='signUp'),
    path('login/',views.login,name='login'),

]