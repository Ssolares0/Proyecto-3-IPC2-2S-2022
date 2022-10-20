
from Lista_RecursosConfig import RecursosConfig
class Configuraciones():
    def __init__(self,idConfiguracion,nombre,descripcion):
        self.idConfiguracion= idConfiguracion
        self.nombre=nombre
        self.descripcion=descripcion
        self.recursosConfiguracion = []

    def addRecursosConfig(self,id,cantidadRecurso):
        nuevo = RecursosConfig(id, cantidadRecurso)
        self.recursosConfiguracion.append(nuevo)

    def obtenerRecursosConfig(self):
        json=[]

        for config in self.recursosConfiguracion:
            config = {
                'id': config.id,
                "Cantidad": config.cantidadRecurso,
                

            }  
            json.append(config)
        return json    
        
        
