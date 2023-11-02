class Socio:
    def __init__(self, nombre, numeroSocio):
        self._nombre = nombre
        self._numeroSocio = numeroSocio
        
    @property
    def numeroSocio(self):
        return self._numeroSocio
    
    @property
    def nombre(self):
        return self._nombre
    
    #def agregarPrestamo(self, prestamo):
        #Aca debería entrar a la bd y consultar por todos los prestamos asociados a este número de socio, ver si son 3 o si alguno esta con demora y no darselo