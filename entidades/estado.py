class Estado:
    def __init__(self, nombre : str, objeto: str, idEstado : int):
        self._nombre = nombre
        self._objeto = objeto
        self._idEstado = idEstado
        
    def Disponible(self):
        self._nombre = "Disponible"
        self._objeto = "Libro"
        return self._nombre
    
    def Prestado(self):
        self._nombre = "Prestado"
        self._objeto = "Libro"
        return self._nombre
    
    def Extraviado(self):
        self._nombre = "Extraviado"
        self._objeto = "Libro"
        return self._nombre
        
    def Disponible(self):
        self._nombre = "Disponible"
        self._objeto = "Libro"
        return self._nombre
    
    def Devuelto(self):
        self._nombre = "Devuelto"
        self._objeto = "Prestamo"
        return self._nombre
    
    def Atrasado(self):
        self._nombre = "Atrasado"
        self._objeto = "Prestamo"
        return self._nombre