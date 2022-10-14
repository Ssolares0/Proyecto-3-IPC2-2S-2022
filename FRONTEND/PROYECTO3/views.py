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

def signUp(request):
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
            response = requests.post(endpoint + 'agregarDatos', data=xml_binary)
            if response.ok:
                response =requests.get(endpoint + 'buscarmensajes')
                buscarmsg = response.json()
                ctx['response'] = buscarmsg
            else:
                ctx['response'] = 'El archivo se envio, pero hubo un error en el servidor'
    else:
        return render(request, 'signUp.html')
    return render(request, 'signUp.html', ctx)

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