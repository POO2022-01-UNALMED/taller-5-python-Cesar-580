class Zona:

    def __init__(self,nombre,zoo= None,animales=None):
        self._nombre = nombre
        self._zoo = zoo
        self._animales = animales

    # Get - Set
    def getNombre(self):
        return self._nombre
    def setNombre(self, nombre):
        self._nombre = nombre

    def getZoo(self):
        return self._zoo
    def setZoo(self, zoo):
        self._zoo = zoo

    def getAnimales(self):
        return self._animales
    def setAnimales(self, animales):
        self._animales = animales

    # Metodos
    def agregarAnimales(self,animal):
        if self._animales == None:
            self._animales = []
        self._animales.append(animal)
    def cantidadAnimales(self):
        return len(self._animales)
    
