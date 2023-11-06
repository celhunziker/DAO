import sqlite3

# Clase Singleton para la conexión a la base de datos
class DatabaseManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseManager, cls).__new__(cls)
            cls._instance.conn = sqlite3.connect('libreria.db')
        return cls._instance
    
    def consultar(self, consultaSQL):
        tabla = None
        cursor = self.conn.cursor()
        cursor.execute(consultaSQL)
        tabla = cursor.fetchall()
        cursor.close()
        self.conn.close()
        return tabla
    
    def actualizar(self, consultaSQL):
        filasAfectadas = 0
        cursor = self.conn.cursor()
        cursor.execute(consultaSQL)
        filasAfectadas = cursor.rowcount
        cursor.close()
        self.conn.commit()
        self.conn.close()
        return filasAfectadas
    
    
    def crear_tablas(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS libros (
            codigo INTEGER PRIMARY KEY, 
            titulo TEXT, 
            precioReposicion REAL, 
            estado TEXT,
            borrado INTEGER)''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS socios (
            numeroSocio INTEGER PRIMARY KEY, 
            nombre TEXT,
            borrado INTEGER)''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS prestamos (
            idPrestamo INTEGER PRIMARY KEY, 
            fechaPrestamo DATE, 
            diasDevolucion INTEGER, 
            diasRetraso INTEGER, 
            devuelto BOOLEAN, 
            socio_numeroSocio INTEGER, 
            libro_codigo INTEGER, 
            borrado INTEGER,
            FOREIGN KEY (socio_numeroSocio) REFERENCES socios (numeroSocio),
            FOREIGN KEY (libro_codigo) REFERENCES libros (codigo))''')
        self.conn.commit()
        cursor.close()