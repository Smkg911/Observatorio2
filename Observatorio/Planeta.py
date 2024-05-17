from SateliteNatural import SateliteNatural
class Planeta: 
    def __init__(self, nombre, distanciaMediaSol,excentricidad,periodoOrbital,velocidadOrbital,inlcinacion):
        self.__nombre = nombre 
        self.__distanciaMediaSol = distanciaMediaSol
        self.__excentricidad = excentricidad
        self.__periodoOrbital = periodoOrbital
        self.__velocidadOrbital = velocidadOrbital
        self.__inclinacion = inlcinacion
        self.__satelites = []
        
    def getNombre(self):
        return self.__nombre
    
    def getDistanciaMedia(self):
        return self.__distanciaMediaSol
    
    def getInclinacion(self):
        return self.__inclinacion
    
    def agregarSateliteNatural(self,nombre,excentricidad,inclinacion):
        agrego = False 
        nuevo = SateliteNatural(nombre,excentricidad,inclinacion)
        self.__satelites.append(nuevo)
        if nuevo is not None:
            agrego = True
        return agrego
    
    def getSatelitesNaturales(self):
        return self.__satelites
    
    def eliminarSatelite(self,nombre):
        self.__satelites.remove(nombre)
        
    def getSatelite(self,nombre):
        return self.__satelite[self.__satelite.index(nombre)]
    
    def editarSateliteNatural(self, nombre, excentricidad, inclinacion):
        for satelite in self.__satelites:
            if satelite.getNombre() == nombre:
                satelite.setExcentricidad(excentricidad)
                satelite.setInclinacionOrbital(inclinacion)