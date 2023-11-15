
from entidades.socio import Socio
from entidades.libro import Libro
from entidades.prestamo import Prestamo
from presentacion.errores import *
from Sqlite import *
from datetime import datetime

def consultarSocio(numero_socio : int):
    lista_socios = consultar_socio(numero_socio)
    if len(lista_socios) == 1:
        return lista_socios[0]
    else:
        raise NroSocioInxistente

def eliminarSocio(socio : Socio):
    eliminar_socio(socio)

def registrarSocio(nombre_socio : str):
    numerosocio = insertar_socio(nombre_socio)
     # Verificar si se obtuvo un número de socio válido
    if numerosocio is not None:
        # Crear el objeto Socio utilizando el número de socio obtenido
        socio = Socio(numerosocio, nombre_socio)
        return socio
    else:
        # Manejar el caso en que no se pudo obtener el número de socio
        return None
    
def registrarLibro(titulo : str, precio : str, estado : str):
    codigo = insertar_libro(titulo,precio,estado)
    if codigo is not None:
        libro = Libro(codigo, titulo, float(precio), estado)
        return libro
    else:
        return None
    
    
def consultarLibro(codigo : int):
    lista_libros = consultar_libro(codigo)
    if len(lista_libros) == 1:
        return lista_libros[0]
    else:
        raise LibroInexistente(codigo)

def eliminarLibro(libro : Libro):
    eliminar_libro(libro)
    
def registrarPrestamo(codigo : str, nroSocio : str, diasPrestamo : str):
    libro = consultarLibro(int(codigo))
    socio = consultarSocio(int(nroSocio))
    # Obtener solo la fecha (sin la hora)
    fecha_actual = datetime.now().date()
    idprestamo = registrar_prestamo(socio.numeroSocio, libro.codigo, fecha_actual, diasPrestamo)
    if idprestamo is not None:
        prestamo = Prestamo(idprestamo, fecha_actual, diasPrestamo, socio, libro, 0)
        return prestamo
    else:
        return None
    
def consultarPrestamo(idPrestamo : str):
    lista_prestamos = consultar_prestamo(idPrestamo)
    if len(lista_prestamos) == 1:
        return lista_prestamos[0]
    else:
        raise PrestamoInexistente(idPrestamo)
    
def registrarDevolucion(idPrestamo : str):
    prestamo = consultarPrestamo(idPrestamo)
    fecha_actual = datetime.now().date()
    if prestamo:
        registrar_devolucion(idPrestamo,fecha_actual)
    else:
        raise PrestamoInexistente(idPrestamo)
    