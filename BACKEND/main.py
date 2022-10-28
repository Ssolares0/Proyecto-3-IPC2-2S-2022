from flask import Flask
import re 
from flask_cors import CORS
from usuario import users

from flask import Flask, jsonify,request
import xml.etree.ElementTree as ET

from manager import Manager

app = Flask(__name__)
usuarios =[]
CORS(app)

admin = users("Sebastian","Solares","Ssolares0","sebas@gmail.com","1234")
usuarios.append(admin)



@app.route('/')



def index():
    return "hola, soy una API"

manage = Manager()


@app.route('/crearUsuario',methods=['POST'])
def crearUser():
    
   usuariorep= False
   passval= False
   caracteres= False

   countCarac= 0
   contCaracteres = 0
   minimoCarac= False

   user = request.get_data()
   nombre = request.json["nombres"]
   nuevouser= (request.json["nombres"], request.json["apellidos"], request.json["username"], request.json["correo"], request.json["contraseña"])
   manage.addUsuarios(request.json["nombres"], request.json["apellidos"], request.json["username"], request.json["correo"], request.json["contraseña"])

   """for x in usuarios:
        if (x.getUsername() == request.json["username"]):
            usuariorep = True

   for x in request.json["contraseña"]:
        if (x == "!") or (x == "@") or (x == "#") or (x == "$") or (
                x == "%") or (x == "^") or (x == "&") or (x == "*") or (
                    x == "(") or (x == ")"):
            caracteres = True
            print("si")

   for x in request.json["contraseña"]:

        contCaracteres = contCaracteres + 1
        if contCaracteres >= 8:
            minimoCarac = True

   if (minimoCarac == True) and (caracteres == True):
        passval = True

   if (usuariorep == False) and (passval == True):
        manage.addUsuarios(request.json["nombres"], request.json["apellidos"], request.json["username"], request.json["correo"], request.json["contraseña"])
        respuesta = jsonify({
            "error": False,
            "mensaje": "Cuenta creada satisfactoriamente"
        })
        return (respuesta)

   else:
        if usuariorep == True:
            respuesta = jsonify({
                "error": True,
                "mensaje": "El usuario ya existe!"
            })
            return (respuesta)

        if passval == False:
            respuesta = jsonify({
                "error":
                True,
                "mensaje":
                "Contrasena no valida: Debe de contener algun caracter y numero"
            })
            return (respuesta)"""


   return jsonify( {"ok": True,"MSG":"USER AGREGADO CON EXITO CON EXITO"})         


@app.route('/crearRecursos', methods=['POST'])

def CrearRecursos():
   recursos = request.get_data()
   print(request.json["idRecurso"], request.json["nombre"], request.json["abreviatura"], request.json["metrica"], request.json["tipo"], request.json["valorxhora"])

   manage.addListaRecursos(request.json["idRecurso"], request.json["nombre"], request.json["abreviatura"], request.json["metrica"], request.json["tipo"], request.json["valorxhora"])


@app.route('/crearCategoria', methods=['POST'])

def crearCategoria():
   categoria = request.get_data()

   manage.addRecursosConfig(request.json["idRecursosConfiguracion"], request.json["cantidad"])
   manage.addListaConfiguraciones(request.json["idConfiguracion"], request.json["nombreConfiguracion"], request.json["descripcionConfiguracion"])
   manage.addListaCategorias(request.json["idCategoria"], request.json["nombreCategoria"], request.json["descripcionCategoria"], request.json["cargaTrabajo"])

@app.route('/crearClientes', methods=['POST'])

def crearClientes():
   clientes= request.get_data()
   manage.addListaInstancias(request.json["idInstancia"], request.json["idConfiguracion"], request.json["nombreInstancia"], request.json["fechaInicio"], request.json["estado"], request.json["fechaFinal"])
   manage.addListaClientes(request.json["nit"], request.json["nombreCliente"], request.json["usuario"], request.json["clave"], request.json["direccion"], request.json["email"])

@app.route('/add', methods=['POST'])

def AgregarDatos():  
   xmlGood =True
   try:
   
      manage.listaRecursos =[]
      manage.listaCategorias = []
      manage.listaClientes = []
      manage.listaConfiguraciones = []
      count= 0

      xml = request.get_data().decode('utf-8')
      
      root = ET.XML(xml)
      
      for p in root:
         if p.tag== "listaRecursos":
            for subp in p:
               manage.addListaRecursos(subp.attrib["id"], subp[0].text, subp[1].text, subp[2].text, subp[3].text, subp[4].text)
               
         elif p.tag =="listaCategorias":
            for subp2 in p:
               for subsubp2 in subp2:
                  for subsubsubp2 in subsubp2:
                     for subsubsubsubp2 in subsubsubp2:
                        for subsubsubsubsubp2 in subsubsubsubp2:
                           
                           manage.addRecursosConfig(subsubsubsubsubp2.attrib["id"],subsubsubsubsubp2.text)
                        count =+1   
                     manage.addListaConfiguraciones(subsubsubp2.attrib["id"], subsubsubp2[0].text, subsubsubp2[1].text)
               
               manage.addListaCategorias(subp2.attrib["id"], subp2[0].text, subp2[1].text, subp2[2].text) 
         elif p.tag =="listaClientes":
            for subp3 in p:
               for subsubp3 in subp3:
                  for subsubsubp3 in subsubp3:
                     texto= subsubsubp3[2].text
                     
                     datos = re.compile(r'(\d+\D\d+\D\d+)')
                     datos2= datos.findall(texto)
                     
                     """texto2= subsubsubp3[4].text
                     datos3 = re.compire(r'(\d+\D\d+\D\d+)')
                     datos4 = datos3.findall(texto2)"""
                     

                     
                     manage.addListaInstancias(subsubsubp3.attrib["id"], subsubsubp3[0].text, subsubsubp3[1].text, datos2[0],subsubsubp3[3].text,subsubsubp3[4].text)
               manage.addListaClientes(subp3.attrib["nit"], subp3[0].text, subp3[1].text, subp3[2].text,subp3[3].text,subp3[4].text)


   except:
      xmlGood = False
   if xmlGood is False:
        mensaje = {
            'ok':False,
            'salida':None
        }
        print("Hay un error!!")
        
        return(jsonify(mensaje))   

   return jsonify( {"ok": True,"MSG":"AGREGADO CON EXITO"})

@app.route('/add2', methods=['POST'])

def AgregarDatos2():  
   xmlGood =True
   try:
   
      manage.listaConsumos = []
      count= 0

      xml = request.get_data().decode('utf-8')
      root = ET.XML(xml)
      
      for p in root:
         manage.addListaConsumos(p.attrib["nitCliente"], p.attrib["idInstancia"], p[0].text, p[1].text)


   except:
      xmlGood = False
   if xmlGood is False:
        mensaje = {
            'ok':False,
            'salida':None
        }
        print("Hay un error!!")
        
        return(jsonify(mensaje))   

   return jsonify( {"ok": True,"MSG":"AGREGADO CON EXITO"})
   
   
               #METODOS GET
@app.route('/buscarlistarecursos', methods=['GET'])

def buscarDatos():
   return jsonify( manage.obtenerListaRecursos())

@app.route('/buscarlistaCategorias', methods=['GET'])

def buscarCategorias():
   return jsonify( manage.obtenerListaCategorias())

@app.route('/buscarlistaClientes', methods=['GET'])

def buscarClientes():
   return jsonify( manage.obtenerListaClientes())

@app.route('/buscarlistaConsumos', methods=['GET'])

def buscarConsumos():
   return jsonify( manage.obtenerListaConsumos())






               #METODOS DELETE
@app.route('/reset', methods=['DELETE'])

def reset():
   manage.reset()
   return jsonify({'msg':'borrado'})

@app.route('/reset2', methods=['DELETE'])

def reset2():
   manage.reset2()
   return jsonify({'msg':'borrado'})

   

@app.route('/buscarUsuario', methods=['GET'])

def buscarUsuarios():
   
   return jsonify(manage.obtenerListaUsers())

   


















if __name__ == '__main__':
    app.run(debug=True,port=4000)