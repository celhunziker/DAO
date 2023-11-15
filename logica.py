from Sqlite import *
from socio import *
from errores import *

def consultarSocio(numero_socio : int):
    lista_socios = consultar_socio(numero_socio)
    if len(lista_socios) == 1:
        return lista_socios[0]
    else:
        raise NroSocioInxistente

def eliminarSocio(socio : Socio):
    eliminar_socio(socio)

def registrarSocio(nombre_socio : str, numero_socio : str):
    #me fijo que no exista uno en bd con el mismo nro
    res = buscar_socio_x_nro(int(numero_socio)) 
    if res[0][0] == 0:
        socio = Socio(nombre_socio, int(numero_socio))
        insertar_socio(socio)
    else:
        raise NroSocioExistente(numero_socio)
    
def registrarLibro(codigo : str, titulo : str, precio : str, estado : str):
    res = buscar_libros_por_codigo(int(codigo))
    if res[0] == 0:
        libro = Libro(int(codigo), titulo, float(precio), estado)
        insertar_libro(libro)
    else:
        raise LibroExistente(codigo)