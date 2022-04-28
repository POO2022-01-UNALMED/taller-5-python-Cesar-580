from zooAnimales.animal import Animal

class Anfibio(Animal):
    ranas = 0
    salamandras = 0
    _listado = []
    
    def __init__(self,nombre,edad,habitat,genero,colorPiel,venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio._listado.append(self)

    # Get - Set
    def getColorPiel(self):
        return self._colorPiel
    def setColorPiel(self, colorPiel):
        self._colorPiel = colorPiel

    def getVenenoso(self):
        return self._venenoso
    def setVenenoso(self,venenoso):
        self._venenoso = venenoso

    def getListado(self):
        return self._listado
    def setListado(self, listado):
        self._listado = listado

    # Metodos
    
    def movimiento(self):
        return "saltar"

    def isVenenoso(self):
        return self._venenoso

    @classmethod
    def cantidadAnfibios(cls):
        return len(cls._listado)

    @classmethod
    def crearRana(cls, nombre, edad, genero):
        Anfibio.ranas += 1
        return Anfibio(nombre, edad, "selva", genero, "rojo",True)

    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        Anfibio.salamandras += 1
        return Anfibio(nombre, edad, "selva", genero, "negro y amarillo",False)