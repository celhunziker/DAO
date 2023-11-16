
from datetime import datetime, timedelta


class Prestamo:
    def __init__(self, idPrestamo, fechaPrestamo, diasDevolucion, diasRetraso, devuelto, numeroSocio, codigo):
        self._idPrestamo = idPrestamo
        self._fechaPrestamo = fechaPrestamo
        self._diasDevolucion = diasDevolucion
        self._socio = numeroSocio
        self._libro = codigo
        self._diasRetraso = diasRetraso
        self._devuelto = devuelto
        
    @property
    def fechaPrestamo(self):
        return self._fechaPrestamo
    
    @property
    def diasDevolucion(self):
        return self._diasDevolucion
    
    @property
    def socio(self):
        return self._socio
    
    @property
    def libro(self):
        return self._libro
    @property
    def diasRetraso(self):
        return self._diasRetraso
    
    @property
    def devuelto(self):
        return self._devuelto
    
    
        
        
    

        
        
        