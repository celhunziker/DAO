class NroSocioExistente(Exception):
    """Se dispara cuando el nro de socio ya existe.
    Atributos:
    salario -- nro socio que disparó el error
    message -- explicación del error
    """
    def __init__(self,
        nroSocio,
        message="El numero de socio ya existe"):
        self._nroSocio = nroSocio
        self._message = message
        super().__init__(self._message)

class NroSocioInxistente(Exception):
    """Se dispara cuando el nro de socio no existe.
    Atributos:
    salario -- salario que disparó el error
    message -- explicación del error
    """
    def __init__(self,
        nroSocio,
        message="El numero de socio no existe"):
        self._nroSocio = nroSocio
        self._message = message
        super().__init__(self._message)

class LibroExistente(Exception):
    """Se dispara cuando el codigo del libro ya existe.
    Atributos:
    codigo -- codigo que disparó el error
    message -- explicación del error
    """
    def __init__(self,
        codigo,
        message="El numero de codigo ya existe"):
        self._codigo = codigo
        self._message = message
        super().__init__(self._message)
    
class LibroInexistente(Exception):
    """Se dispara cuando el codigo del libro no existe.
    Atributos:
    codigo -- codigo que disparó el error
    message -- explicación del error
    """
    def __init__(self,
        codigo,
        message="El libro no existe"):
        self._codigo = codigo
        self._message = message
        super().__init__(self._message)
        
class PrestamoInexistente(Exception):
    """Se dispara cuando el codigo del libro no existe.
    Atributos:
    codigo -- codigo que disparó el error
    message -- explicación del error
    """
    def __init__(self,
        codigo,
        message="El Prestamo no existe"):
        self._codigo = codigo
        self._message = message
        super().__init__(self._message)

class LibroNoDisponible(Exception):
        def __init__(self,
            codigo,
            message="El libro no está disponible"):
            self._codigo = codigo
            self._message = message
            super().__init__(self._message)