import sqlite3

conn = sqlite3.connect('libreria.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS libros (
    codigo INTEGER PRIMARY KEY, 
    titulo TEXT, 
    precioReposicion REAL, 
    estado TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS socios (
    numeroSocio INTEGER PRIMARY KEY, 
    nombre TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS prestamos (
    idPrestamo INTEGER PRIMARY KEY, 
    fechaPrestamos DATE, 
    diasDevolucion INTEGER, 
    diasRetraso INTEGER, 
    devuelto BOOLEAN, 
    socio_numeroSocio INTEGER, 
    libro_codigo INTEGER, 
    FOREIGN KEY (socio_numeroSocio) REFERENCES socios (numeroSocio),
    FOREIGN KEY (libro_codigo) REFERENCES libros (codigo))''')

conn.commit()

cursor.close()
conn.close()

#hasta aca

def insertarLibro(self, libro):
    cursor = conn.cursor()
    codigo = int(libro.codigo)
    titulo = str(libro.titulo)
    precioReposicion = float(libro.precioReposicion)
    estado = str(libro.estado)
    cursor.execute("INSERT INTO libros (codigo, titulo, precioResposicion, estado) VALUES (?, ?, ?, ?)", (codigo, titulo, precioReposicion, estado))
    conn.commit()
    cursor.close()
    conn.close()

def insertarSocio(self, socio):
    cursor = conn.cursor()
    numeroSocio = int(socio.numeroSocio)
    nombre = str(socio.nombre)
    cursor.execute("INSERT INTO libros (numeroSocio, nombre) VALUES (?, ?)", (numeroSocio, nombre))
    conn.commit()
    cursor.close()
    conn.close()
    
def insertarPrestamos(self, libro, socio, prestamo):
    cursor = conn.cursor()
    idPrestamo = int(prestamo.idPrestamo)
    fechaPrestamo = prestamo.fechaPrestamo
    diasDevolucion = int(prestamo.diasDevolucion)
    diasRetraso = int(prestamo.diasRetraso)
    devuelto = bool(prestamo.devuelto)
    numeroSocio = int(socio.numeroSocio)
    codigo = int(libro.codigo)
    cursor.execute('''INSERT INTO prestamos (
        idPrestamos, fechaPrestamo, diasDevolucion, diasRetraso, devuelto, socio_numeroSocio, libro_codigo) 
        VALUES (?, ?, ?, ?, ?, ?, ?)''', (idPrestamo, fechaPrestamo, diasDevolucion, diasRetraso, devuelto, numeroSocio, codigo))
    conn.commit()
    cursor.close()
    conn.close()

def actualizarPrestamos(self, prestamo):
    cursor = conn.cursor()
    idPrestamo = int(prestamo.idPrestamo)
    fechaPrestamo = prestamo.fechaPrestamo
    diasDevolucion = int(prestamo.diasDevolucion)
    diasRetraso = int(prestamo.diasRetraso)
    devuelto = bool(prestamo.devuelto)
    numeroSocio = int(socio.numeroSocio)
    codigo = int(libro.codigo)
    cursor.execute('''UPDATE prestamos (
        idPrestamos, fechaPrestamo, diasDevolucion, diasRetraso, devuelto, socio_numeroSocio, libro_codigo) 
        SET (?, ?, ?, ?, ?, ?, ?)''', (idPrestamo, fechaPrestamo, diasDevolucion, diasRetraso, devuelto, numeroSocio, codigo))
    conn.commit()
    cursor.close()
    conn.close()

'''cursor.execute("SELECT * FROM empleados")
resultado = cursor.fetchall()
for fila in resultado:
    print(f"ID: {fila[0]}, Nombre: {fila[1]}, Salario: {fila[2]}")'''



