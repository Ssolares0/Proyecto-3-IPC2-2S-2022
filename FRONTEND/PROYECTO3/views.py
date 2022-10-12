from django.shortcuts import render


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