
from Lista_Recursos import Recursos
from Lista_Categorias import Categorias
from Lista_Configuraciones import Configuraciones
from Lista_RecursosConfig import RecursosConfig
from Lista_Clientes import Cliente
from Lista_Instancias import Instancias
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
        self.listaRecursosConfig =[]
        self.listaInstanci = []

    def addListaRecursos(self,idRecurso, nombre, abreviatura, metrica, tipo, valorxhora):
        new = Recursos(idRecurso, nombre, abreviatura, metrica, tipo, valorxhora)
        self.listaRecursos.append(new)

    def addListaCategorias(self,idCategoria, nombre, descripcion, cargaTrabajo):
        new = Categorias(idCategoria, nombre, descripcion, cargaTrabajo)
        new.lista_configuraciones = self.listaConfiguraciones.copy()
        self.listaConfiguraciones = []
        
        self.listaCategorias.append(new)
        
    def addListaConfiguraciones(self,idConfiguracion,nombre,descripcion):
        new = Configuraciones(idConfiguracion, nombre, descripcion)
        new.recursosConfiguracion = self.listaRecursosConfig.copy()
        self.listaRecursosConfig= []
        self.listaConfiguraciones.append(new)    

    def addRecursosConfig(self,idRecurso,cantidadRecurso):
        new = RecursosConfig(idRecurso, cantidadRecurso)
        self.listaRecursosConfig.append(new)

    def addListaClientes(self,nit,nombre,usuario,clave,direccion,correo):    
        new= Cliente(nit, nombre, usuario, clave, direccion, correo)
        new.listaInstancias = self.listaInstanci.copy()
        self.listaInstanci=[]
        self.listaClientes.append(new)

    def addListaInstancias(self,idInstancia,idConfiguracion,nombre,fechaInicio,estado,fechaFinal):
        new= Instancias(idInstancia, idConfiguracion, nombre, fechaInicio, estado, fechaFinal)
        self.listaInstanci.append(new)




    


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
                "lista Configuraciones": Categorias.obtenerListaConfig()

                



            }
            json.append(Categorias)
        print(json)
        return json

    def obtenerListaClientes(self):
        json= []
        for Clientes in self.listaClientes:
            Clientes ={
                "Nit": Clientes.nit,
                "Nombre":Clientes.nombre,
                "Usuario": Clientes.usuario,
                "Clave": Clientes.clave,
                "direccion":Clientes.direccion,
                "Correo": Clientes.correo,
                "lista Instancias": Clientes.obtenerListaInstancias()






            }
            json.append(Clientes)
        return json    

    def reset(self):
        self.listaRecursos =[]
        self.listaCategorias = []
        self.listaClientes = []
        self.listaConfiguraciones =[]
        self.listaRecursosConfig =[]
        self.listaInstanci = []

