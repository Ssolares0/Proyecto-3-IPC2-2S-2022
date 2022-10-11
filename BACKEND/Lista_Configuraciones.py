
from Lista_RecursosConfig import RecursosConfig
class Configuraciones():
    def __init__(self,idConfiguracion,nombre,descripcion):
        self.idConfiguracion= idConfiguracion
        self.nombre=nombre
        self.descripcion=descripcion
        self.recursosConfiguracion = []

    def addRecursosConfig():
        nuevo = RecursosConfig(id, cantidadRecurso)
        self.recursosConfiguracion.append(nuevo)

    def obtenerRecursosConfig():
        json=[]

        for config in self.recursosConfiguracion:
            config = {
                'id': config.recursosConfiguracion,
                

            }  
            json.append(config)
        return json    
        
        
