from flask import Flask
import re 
from flask_cors import CORS

from flask import Flask, jsonify,request
import xml.etree.ElementTree as ET

from manager import Manager

app = Flask(__name__)
CORS(app)
@app.route('/')



def index():
    return "hola, soy una API"

manage = Manager()





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
               print(subp.attrib["id"], subp[0].text, subp[1].text, subp[2].text, subp[3].text, subp[4].text)
         elif p.tag =="listaCategorias":
            for subp2 in p:
               for subsubp2 in subp2:
                  for subsubsubp2 in subsubp2:
                     """for subsubsubsubp2 in subsubsubp2:
                        for subsubsubsubsubp2 in subsubsubsubp2:
                           
                           manage.listaConfiguraciones[count].addRecursosConfig(subsubsubsubsubp2.attrib["id"],subsubsubsubsubp2.text)
                        count =+1   """
                     manage.addListaConfiguraciones(subsubsubp2.attrib["id"], subsubsubp2[0].text, subsubsubp2[1].text)
               
               manage.addListaCategorias(subp2.attrib["id"], subp2[0].text, subp2[1].text, subp2[2].text)      

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
   

@app.route('/buscarlistarecursos', methods=['GET'])

def buscarDatos():
   return jsonify( manage.obtenerListaRecursos())

@app.route('/buscarlistaCategorias', methods=['GET'])

def buscarCategorias():
   return jsonify( manage.obtenerListaCategorias())


















if __name__ == '__main__':
    app.run(debug=True,port=4000)