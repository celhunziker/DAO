import sqlite3

conn = sqlite3.connect('mi_base_de_datos.db')

cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS empleados (id INTEGER PRIMARY KEY, nombre TEXT, salario REAL)")

cursor.execute("INSERT INTO empleados (nombre, salario) VALUES (?, ?)", ("JUAN", 23))

conn.commit()

cursor.execute("SELECT * FROM empleados")
resultado = cursor.fetchall()
for fila in resultado:
    print(f"ID: {fila[0]}, Nombre: {fila[1]}, Salario: {fila[2]}")



cursor.close()
conn.close()