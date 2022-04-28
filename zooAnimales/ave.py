from zooAnimales.animal import Animal

class Ave(Animal):
    halcones = 0
    aguilas = 0
    _listado = []

    def __init__(self,nombre,edad,habitat,genero,colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave._listado.append(self)

    # Get - Set
    def getColorPlumas(self):
        return self._colorPlumas
    def setNombre(self, colorPlumas):
        self._colorPlumas = colorPlumas

    def getListado(self):
        return self._listado
    def setListado(self, listado):
        self._listado = listado

    # Metodos
    def movimiento(self):
        return "volar"
    
    @classmethod
    def cantidadAves(cls):
        return len(cls._listado)

    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        Ave.halcones += 1
        return Ave(nombre, edad, "montanas", genero, "cafe glorioso")

    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        Ave.aguilas += 1
        return Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
