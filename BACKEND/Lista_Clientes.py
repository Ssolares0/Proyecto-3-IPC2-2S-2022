
from Lista_Instancias import Instancias
class Cliente():
    def __init__(self,nit,nombre,usuario,clave,direccion,correo):
        self.nit = nit
        self.nombre = nombre
        self.usuario = usuario
        self.clave = clave
        self.direccion = direccion
        self.correo= correo
        self.listaInstancias= []

    def addListaInstancias(self,idInstancia, idConfiguracion, nombre, fechaInicio, estado, fechaFinal):
        nuevo = Instancias(idInstancia, idConfiguracion, nombre, fechaInicio, estado, fechaFinal)
        self.listaInstancias.append(nuevo)

    def obtenerListaInstancias(self):
        json=[]

        for config in self.listaInstancias:
            config2={
                "ID instancia": config.idInstancia,
                "ID CONFIGURACION": config.idConfiguracion,
                "Nombre": config.nombre,
                "Fecha Inicio": config.fechaInicio,
                "Estado": config.estado,
                "Fecha Final": config.fechaFinal,
                


            }    
            json.append(config2)
        return json    


