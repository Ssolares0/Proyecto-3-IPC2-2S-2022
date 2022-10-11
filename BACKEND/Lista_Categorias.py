
from Lista_Configuraciones import Configuraciones
from Lista_RecursosConfig import RecursosConfig
class Categorias():
    def __init__(self,idCategoria,nombre,descripcion,cargaTrabajo):
        self.nombre=nombre
        self.idCategoria=idCategoria
        self.descripcion=descripcion
        self.cargaTrabajo=cargaTrabajo
        self.lista_configuraciones= []

    def addListaConfig(self,s):
        nuevo = Configuraciones(idConfiguracion, nombre, descripcion)
        self.lista_configuraciones.append(nuevo)

    def obtenerListaConfig():
        json = []
        for config in self.lista_configuraciones:
            config = {
                'idConfiguracion': config.lista_configuraciones,
                
                'Nombre': config.lista_configuraciones,
                "descripcion": config.lista_configuraciones,
                #"Recurso": config.obtenerRecursosConfig()
                

            }
            json.append(config)

        return json    



