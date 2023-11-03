from libro import Libro
from socio import Socio
from datetime import datetime, timedelta

def Prestamo(Socio, Libro):
    def __init__(self, idPrestamo, fechaPrestamo, diasDevolucion, diasRetraso, devuelto):
        self._idPrestamo = idPrestamo
        self._fechaPrestamo = fechaPrestamo
        self._diasDevolucion = diasDevolucion
        self._diasRetraso = diasRetraso
        self._devuelto = devuelto
        
    @property
    def fechaPrestamo(self):
        return self._fechaPrestamo
    
    @property
    def diasDevolucion(self):
        return self._diasDevolucion
    
    @property
    def diasRetraso(self):
        if fechaPrestamo.date + timedelta(days=diasDevolucion) <= datetime.now().date:
            return 0
        else:
            retraso = datetime.now().date - (fechaPrestamo.date + timedelta(days=diasDevolucion))
            return retraso.days
    
    @property
    def devuelto(self):
        return self._devuelto
    
    
        
        
    

        
        
        