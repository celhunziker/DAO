from db.bdManager import DatabaseManager
from entidades.socio import *
from entidades.libro import *
from entidades.prestamo import *

# Funciones para la administración de libros
def insertar_libro(titulo, precio, estado):
    db_manager = DatabaseManager()
    titulo = str(titulo)
    precio_reposicion = float(precio)
    estado = str(estado)
    query = f"INSERT INTO libros (titulo, precioReposicion, estado, borrado) " \
            f"VALUES ('{titulo}', {precio_reposicion}, '{estado}', 0)"
    db_manager.actualizar(query)
    codigo = db_manager.obtener_ultimo_id_insertado_libros()
    return codigo
    

def actualizar_libro(libro : Libro):
    db_manager = DatabaseManager()
    codigo = int(libro.codigo)
    titulo = str(libro.titulo)
    precio_reposicion = float(libro.precioReposicion)
    estado = str(libro.estado)
    query = f"UPDATE libros SET titulo = '{titulo}', precioReposicion = {precio_reposicion}, estado = '{estado}' WHERE codigo = {codigo}"
    db_manager.actualizar(query)

def eliminar_libro(libro : Libro):
    db_manager = DatabaseManager()
    codigo = int(libro.codigo)
    query = f"UPDATE libros SET borrado = 1 WHERE codigo = {codigo}"
    db_manager.actualizar(query)

def consultar_libro(codigo : int):
    query = f"SELECT * FROM libros where codigo = {codigo} and borrado = 0"
    db_manager = DatabaseManager()
    resultados = db_manager.consultar(query)
    libros = [Libro(codigo=row[0], titulo=row[1], precioReposicion=row[2], estado=row[3]) for row in resultados]
    return libros

def consultar_libros():
    query = f"SELECT * FROM libros"
    db_manager = DatabaseManager()
    resultados = db_manager.consultar(query)
    return resultados

def buscar_libros_por_titulo(titulo):
    query = f"SELECT * FROM libros WHERE titulo = '{titulo}'"
    db_manager = DatabaseManager()
    resultados = db_manager.consultar(query)
    libros = [Libro(codigo=row[0], titulo=row[1], precioReposicion=row[2], estado=row[3]) for row in resultados]
    return libros

def buscar_libros_por_codigo(codigo):
    query = f"SELECT count(1) FROM libros WHERE codigo = '{codigo}'"
    db_manager = DatabaseManager()
    resultados = db_manager.consultar(query)
    return resultados[0]


# Funciones para la administración de socios
def buscar_socio_x_nro(numero_socio : int):
    query = f"SELECT count(1) FROM socios where numeroSocio = {numero_socio} and borrado = 0"
    db_manager = DatabaseManager()
    resultados = db_manager.consultar(query)
    return resultados

def insertar_socio(nombresocio):
    db_manager = DatabaseManager()
    nombre = nombresocio
    query = f"INSERT INTO socios (nombre, borrado) VALUES ('{nombre}', 0)"
    db_manager.actualizar(query)
    numero_socio = db_manager.obtener_ultimo_id_insertado_socios()
    return numero_socio

def consultar_socio(numero_socio : int):
    query = f"SELECT * FROM socios where numeroSocio = {numero_socio} and borrado = 0"
    db_manager = DatabaseManager()
    resultados = db_manager.consultar(query)
    socios = [Socio(numeroSocio=row[0], nombre=row[1]) for row in resultados]
    return socios

def actualizar_socio(socio : Socio):
    db_manager = DatabaseManager()
    numero_socio = int(socio.numeroSocio)
    nombre = str(socio.nombre)
    query = f"UPDATE socios SET nombre = '{nombre}' WHERE numeroSocio = {numero_socio}"
    db_manager.actualizar(query)

def eliminar_socio(socio : Socio):
    db_manager = DatabaseManager()
    numero_socio = int(socio.numeroSocio)
    query = f"UPDATE socios SET borrado = 1 WHERE numeroSocio = {numero_socio}"
    db_manager.actualizar(query)

def listar_socios():
    query = "SELECT * FROM socios"
    db_manager = DatabaseManager()
    resultados = db_manager.consultar(query)
    socios = [Socio(numeroSocio=row[0], nombre=row[1]) for row in resultados]
    return socios

def listar_socios():
    query = "SELECT * FROM socios"
    db_manager = DatabaseManager()
    resultados = db_manager.consultar(query)
    return resultados

# Funciones para la registración de préstamos y devoluciones
def registrar_prestamo(socio_id, libro_id, fecha_prestamo, dias_devolucion):
    db_manager = DatabaseManager()
    query = f"INSERT INTO prestamos (socio_numeroSocio, libro_codigo, fechaPrestamo, diasDevolucion, devuelto, borrado) " \
            f"VALUES ({int(socio_id)}, {int(libro_id)}, '{fecha_prestamo}', {int(dias_devolucion)}, 0, 0)"
    query2 = f"UPDATE libros SET estado = PRESTADO where codigo = {libro_id}
    db_manager.actualizar(query)
    db_manager.actualizar(query2)
    idPrestamo = db_manager.obtener_ultimo_id_insertado_prestamo()
    return idPrestamo

def consultar_prestamo(idPrestamo):
    query = f"SELECT * FROM prestamos where idPrestamo = {idPrestamo} and borrado = 0"
    db_manager = DatabaseManager()
    resultados = db_manager.consultar(query)
        
    prestamos = []
    for row in resultados:
        prestamo = Prestamo(idPrestamo=row[0], fechaPrestamo=row[1], diasDevolucion=row[2], diasRetraso=row[3], devuelto=row[4], numeroSocio=row[5], codigo=row[6])
        prestamos.append(prestamo)

    return prestamos



def registrar_devolucion(prestamo_id, fecha_devolucion):
    db_manager = DatabaseManager()

    # Obtener el valor actual de diasRetrasoEnDevolucion
    query_obtener_dias_retraso = f"SELECT diasRetraso FROM prestamos WHERE idPrestamo = {prestamo_id}"
    result = db_manager.consultar(query_obtener_dias_retraso)

    # Verificar que se obtuvo un resultado válido
    if result and result[0] and result[0][0] is not None:
        dias_retraso_en_devolucion = result[0][0]

        # Actualizar la tabla prestamos
        query_actualizar_prestamo = f"UPDATE prestamos SET fechaDevolucion = '{fecha_devolucion}',  devuelto = 1, " \
                                    f"diasRetrasoEnDevolucion = {dias_retraso_en_devolucion} " \
                                    f"WHERE idPrestamo = {prestamo_id}"
        db_manager.actualizar(query_actualizar_prestamo)
    else:
        # Manejar el caso en que no se obtuvo un valor válido
        print("Error: No se pudo obtener el valor de diasRetrasoEnDevolucion.")

# Función para eliminar un préstamo
def eliminar_prestamo(idPrestamo):
    db_manager = DatabaseManager()
    query = f"UPDATE prestamos SET borrado = 1 WHERE idPrestamo = {idPrestamo}"
    db_manager.actualizar(query)

# Funciones para los reportes
def listar_cantidad_libros_estado():
    db_manager = DatabaseManager()
    query = "SELECT estado, COUNT(*) AS cantidad FROM libros GROUP BY estado"
    resultados = db_manager.consultar(query)
    return resultados

def sumatoria_precio_reposicion_librExtraviados():
    db_manager = DatabaseManager()
    query = "SELECT SUM(precioReposicion) AS sumatoria FROM libros WHERE estado = 'Extraviado'"
    resultados = db_manager.consultar(query)
    return resultados

def solicitantes_por_titulo_libro(titulo):
    db_manager = DatabaseManager()
    query = f"SELECT s.numeroSocio, s.nombre FROM socios s " \
            f"INNER JOIN prestamos p ON s.numeroSocio = p.socio_numeroSocio " \
            f"INNER JOIN libros l ON p.libro_codigo = l.codigo " \
            f"WHERE l.titulo = '{titulo}'"
    resultados = db_manager.consultar(query)
    return resultados

def listar_prestamos_por_socio(numeroSocio):
    db_manager = DatabaseManager()
    query = f"SELECT p.idPrestamo, p.fechaPrestamo, p.diasDevolucion, p.devuelto, " \
            f"l.codigo AS codigo_libro, l.titulo AS titulo_libro " \
            f"FROM prestamos p " \
            f"INNER JOIN libros l ON p.libro_codigo = l.codigo " \
            f"WHERE p.socio_numeroSocio = {numeroSocio}"
    resultados = db_manager.consultar(query)
    return resultados

def listar_prestamos_demorados():
    db_manager = DatabaseManager()
    query = "SELECT p.idPrestamo, p.fechaPrestamo, p.diasDevolucion, p.devuelto, " \
            "l.codigo AS codigo_libro, l.titulo AS titulo_libro, s.numeroSocio, s.nombre AS nombre_socio " \
            "FROM prestamos p " \
            "INNER JOIN libros l ON p.libro_codigo = l.codigo " \
            "INNER JOIN socios s ON p.socio_numeroSocio = s.numeroSocio " \
            "WHERE p.devuelto = 0 AND DATE('now') > DATE(p.fechaPrestamo, '+' || p.diasDevolucion || ' days')"
    resultados = db_manager.consultar(query)
    return resultados

def crear_tablas():
    db_manager = DatabaseManager()