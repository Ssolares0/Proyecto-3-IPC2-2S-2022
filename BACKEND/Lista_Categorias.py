
from Lista_Configuraciones import Configuraciones
from Lista_RecursosConfig import RecursosConfig
class Categorias():
    def __init__(self,idCategoria,nombre,descripcion,cargaTrabajo):
        self.nombre=nombre
        self.idCategoria=idCategoria
        self.descripcion=descripcion
        self.cargaTrabajo=cargaTrabajo
        self.lista_configuraciones= []

    def addListaConfig(self,idConfiguracion, nombre, descripcion):
        nuevo = Configuraciones(idConfiguracion, nombre, descripcion)
        self.lista_configuraciones.append(nuevo)

    def obtenerListaConfig(self):
        json = []
        for config in self.lista_configuraciones:
            config2 = {
                'idConfiguracion': config.idConfiguracion,
                
                'Nombre': config.nombre,
                "descripcion": config.descripcion,
                "Recursos Configuracion": config.obtenerRecursosConfig()
                
                

            }
            json.append(config2)

        return json    



