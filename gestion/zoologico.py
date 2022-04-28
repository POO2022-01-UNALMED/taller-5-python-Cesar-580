class Zoologico:

    def __init__(self,nombre,ubicacion,zonas=[]):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = zonas

    # Get - Set
    def getNombre(self):
        return self._nombre
    def setNombre(self, nombre):
        self._nombre = nombre

    def getUbicacion(self):
        return self._ubicacion
    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion
    
    def getZona(self):
        return self._zonas
    def setZona(self, zonas):
        self._zonas = zonas

    # Metodos

    def cantidadTotalAnimales(self):
        con = 0
        for zona in self._zonas:
            con +=  zona.cantidadAnimales()
        return con
    
    def agregarZonas(self,zona):
        self._zonas.append(zona)