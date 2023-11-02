class Libro:
    def __init__(self, codigo, titulo, precioReposicion, estado):
        self._codigo = codigo
        self._titulo = titulo
        self._precioReposicion = precioReposicion
        self._estado = estado
        
    @property
    def codigo(self):
        return self._legajo
    
    @property
    def titulo(self):
        return self._titulo
    
    @property
    def precioReposicion(self):
        return self._precioReposicion
    
    @property
    def estado(self):
        return self._estado
    
    def __str__(self) -> str:
        return f"Datos del Libro:\n\tCódigo: {self.codigo}\n\tTítulo: {self.titulo}\n\tPrecio de Reposición: ${str(self.precioReposicion)}\n\tEstado: {self.estado}"
    
    def estadoDisponible(self):
        self._estado = "Disponible"
        
    def estadoPrestado(self):
        self._estado = "Prestado"
    
    def estadoExtraviado(self):
        self._estado = "Extraviado"
        
    #para ver si esta extraviado tenemos que ingresar a bd y verificar si hay algun prestamo con su codigo y que más de 30 días de demora.
    
