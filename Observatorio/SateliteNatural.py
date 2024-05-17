class SateliteNatural:
    
    def __init__(self, nombre, excentricidad, inclinacionOrbital):
        self.__nombre = nombre
        self.__excentricidad = excentricidad
        self.__inclinacionOrbital = inclinacionOrbital
    
    def getNombre(self):
        return self.__nombre
    
    def getExcentricidad(self):
        return self.__excentricidad
    
    def getInlcinacionOrbital(self):
        return self.__inclinacionOrbital
    
    def setExcentricidad(self,excentricidad):
        self.__excentricidad = excentricidad
        
    def setInclinacionOrbital(self,Inclinacion):
        self.__inclinacionOrbital = Inclinacion
        

        