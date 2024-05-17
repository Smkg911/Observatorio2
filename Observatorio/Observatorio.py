from Planeta import Planeta
class Observatorio:
    
    CANTIDAD_PLANETAS = 8
    NOMBRES_PLANETAS = {
        "Mercurio" : "Mercurio",
        "Venus" : "Venus",
        "Tierra" : "Tierra",
        "Marte" : "Marte",
        "Jupiter" : "Júpiter",
        "Saturno" : "Saturno",
        "Urano" : "Urano",
        "Nemptuno" : "Neptuno"
    }
    
    def __init__(self): 
        self.__planetas = []
    
    def getNombrePlanetas(self): 
        nombresPlanetas = []
        for nombres in self.NOMBRES_PLANETAS.items():
            keys = nombres[0]
            nombresPlanetas.append(keys)
        return nombresPlanetas
    
    def getSateliteNatural(self,nombre):
        return Planeta.getSatelite(nombre)
    
    def getSatelitePorDistancia(self,distancia): 
        return Planeta.getSatelite(distancia)
    
    def getSatelitePorInclinacion(self,inclinacion): 
        return Planeta.getSatelite(inclinacion)
    
    def agregarSateliteNatural(self, nombre, excentricidad, inclinacion):
        Planeta.agregarSateliteNatural(nombre,excentricidad,inclinacion)
        return Planeta.agregarSateliteNatural(nombre,excentricidad,inclinacion)
    
    def eliminarSatelite(self,nombre):
        Planeta.eliminarSatelite(nombre)
    
    def editarSatelite(self,nombre, excentricidad, inclinacion):
        Planeta.agregarSateliteNatural(nombre, excentricidad, inclinacion)
        
            