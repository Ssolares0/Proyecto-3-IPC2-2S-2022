
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
                "IDinstancia": config.idInstancia,
                "IDCONFIGURACION": config.idConfiguracion,
                "Nombre": config.nombre,
                "FechaInicio": config.fechaInicio,
                "Estado": config.estado,
                "FechaFinal": config.fechaFinal,
                


            }    
            json.append(config2)
        return json    


