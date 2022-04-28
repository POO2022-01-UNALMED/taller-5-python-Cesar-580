from zooAnimales.animal import Animal

class Mamifero(Animal):
    caballos = 0
    leones = 0
    _listado = []

    def __init__(self,nombre,edad,habitat,genero,pelaje,patas):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero._listado.append(self)

    # Get - Set
    def getPelaje(self):
        return self._pelaje
    def setNombre(self, pelaje):
        self._pelaje = pelaje

    def getPatas(self):
        return self._patas
    def setPatas(self, patas):
        self._patas = patas
    
    def getListado(self):
        return self._listado
    def setListado(self, listado):
        self._listado = listado

    # Metodos
    def isPelaje(self):
        return self._pelaje
    
    @classmethod
    def cantidadMamiferos(cls):
        return len(cls._listado)

    @classmethod
    def crearCaballo(cls,nombre,edad,genero):
        Mamifero.caballos += 1
        return Mamifero(nombre,edad,"pradera",genero,True,4)

    @classmethod
    def crearLeon(cls,nombre,edad,genero):
        Mamifero.leones += 1
        return Mamifero(nombre,edad,"selva",genero,True,4)
