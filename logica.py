
from entidades.socio import Socio
from entidades.libro import Libro
from entidades.prestamo import Prestamo
from presentacion.errores import *
from Sqlite import *
from datetime import datetime
from presentacion.reportes import *

def consultarSocio(numero_socio : int):
    lista_socios = consultar_socio(numero_socio)
    if len(lista_socios) == 1:
        return lista_socios[0]
    else:
        raise NroSocioInxistente

def listarSocios():
    lista_socios = listar_socios()
    return lista_socios

def eliminarSocio(socio : Socio):
    eliminar_socio(socio)
    
def listarPrestamos():
    prestamos = consultar_prestamos()
    return prestamos

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
    
def listarLibros():
    libros = consultar_libros()
    return libros
    
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
    if libro.estado == "DISPONIBLE":
        idprestamo = registrar_prestamo(socio.numeroSocio, libro.codigo, fecha_actual, diasPrestamo)
        if idprestamo is not None:
            prestamo = Prestamo(idprestamo, fecha_actual, diasPrestamo, None, socio, libro, 0)
            return prestamo
        else:
            raise LibroNoDisponible(codigo)
    else:
        raise LibroNoDisponible(codigo)
    
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
        registrar_devolucion(idPrestamo,fecha_actual,prestamo.libro)
    else:
        raise PrestamoInexistente(idPrestamo)

def generar_reporte_prest_socios(nroSocio: str):
    prestamos = listar_prestamos_por_socio(nroSocio)
    nombreSocio = consultar_nombre_socio(nroSocio)
    generar_reporte_prestamos_x_socio(prestamos, nroSocio, nombreSocio)


def generar_reporte_libros_x_est():
    lista = listar_cantidad_libros_estado()
    generar_reporte_libros_x_estado(lista)

def generar_reporte_sum_precio_extra():
    sumatoria = sumatoria_precio_reposicion_librExtraviados() or 0
    reporte_precio_extraviados(sumatoria)
    
def buscar_solicitantes_x_libro(titulo):
    listaLibros = buscar_libros_por_titulo(titulo)
    listaSolicitantes = list()
    if len(listaLibros) > 0:
        listaSolicitantes = solicitantes_por_titulo_libro(titulo)
        return listaSolicitantes
    else:
        raise LibroInexistente(titulo)

def generar_reporte_solicitantes_de_titulo(lista_solicitantes, titulo):
    generar_reporte_solic_de_titulo(lista_solicitantes, titulo)

def generar_reporte_prestamos_demor():
    lista_demorados = listar_prestamos_demorados()
    generar_reporte_prest_demorados(lista_demorados) 
    
def modificarLibro(codigo, titulo, precio, estado):
    libro = Libro(codigo, titulo, precio, estado)
    actualizar_libro(libro)
    
def modificarSocio(numero, nombre):
    socio = Socio(nombre, numero)
    actualizar_socio(socio)