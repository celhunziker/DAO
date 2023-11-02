import sqlite3

conn = sqlite3.connect('libreria.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS libros (
    codigo INTEGER PRIMARY KEY, 
    titulo TEXT, 
    precioReposicion REAL, 
    stado TEXT)''')

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

#hasta aca

cursor.execute("INSERT INTO empleados (nombre, salario) VALUES (?, ?)", ("JUAN", 23))

conn.commit()

cursor.execute("SELECT * FROM empleados")
resultado = cursor.fetchall()
for fila in resultado:
    print(f"ID: {fila[0]}, Nombre: {fila[1]}, Salario: {fila[2]}")



cursor.close()
conn.close()