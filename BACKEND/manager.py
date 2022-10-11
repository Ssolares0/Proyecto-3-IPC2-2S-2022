
from Lista_Recursos import Recursos
from Lista_Categorias import Categorias
from Lista_Configuraciones import Configuraciones
def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

def remove_punctuation ( text ):
        return re.sub('[%s]' % re.escape(string.punctuation), ' ', text)


class Manager():
    def __init__(self):
        self.listaRecursos =[]
        self.listaCategorias = []
        self.listaClientes = []
        self.listaConfiguraciones =[]

    def addListaRecursos(self,idRecurso, nombre, abreviatura, metrica, tipo, valorxhora):
        new = Recursos(idRecurso, nombre, abreviatura, metrica, tipo, valorxhora)
        self.listaRecursos.append(new)

    def addListaCategorias(self,idCategoria, nombre, descripcion, cargaTrabajo):
        new = Categorias(idCategoria, nombre, descripcion, cargaTrabajo)
        self.listaCategorias.append(new)

    def addListaConfiguraciones(self,idConfiguracion,nombre,descripcion):
        new = Configuraciones(idConfiguracion, nombre, descripcion)
        self.listaConfiguraciones.append(new)


    def obtenerListaRecursos(self):
        json = []
        for Recursos in self.listaRecursos:
            Recursos = {
                "id": Recursos.idRecurso,
                "nombre": Recursos.nombre,
                "abreviatura":Recursos.abreviatura,
                "metrica":Recursos.metrica,
                "tipo": Recursos.tipo,
                "valorxhora":Recursos.valorxhora,



            }
            json.append(Recursos)
        return json

    def obtenerListaCategorias(self):
        json = []
        for Categorias in self.listaCategorias:
            Categorias = {
                "id": Categorias.idCategoria,
                "nombre": Categorias.nombre,
                "descripcion":Categorias.descripcion,
                "Carga de trabajo":Categorias.cargaTrabajo,
                #"lista Condiguraciones": Categorias.obtenerListaConfig

                



            }
            json.append(Categorias)
        return json


    def reset():
        self.listaRecursos =[]
        self.listaCategorias = []
        self.listaClientes = []

