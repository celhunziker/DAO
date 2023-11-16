import sqlite3

# Clase Singleton para la conexión a la base de datos
class DatabaseManager:
    _instance = None
    conn = sqlite3.connect('libreria.db')

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseManager, cls).__new__(cls)
        return cls._instance
    
    def abrir_nueva_conexion(self):
        self.conn = sqlite3.connect('libreria.db')

    def consultar(self, consultaSQL):
        tabla = None
        self.abrir_nueva_conexion()
        cursor = self.conn.cursor()
        cursor.execute(consultaSQL)
        tabla = cursor.fetchall()
        cursor.close()
        self.conn.close()
        return tabla
    
    def actualizar(self, consultaSQL):
        filasAfectadas = 0
        self.abrir_nueva_conexion()
        cursor = self.conn.cursor()
        cursor.execute(consultaSQL)
        filasAfectadas = cursor.rowcount
        cursor.close()
        self.conn.commit()
        self.conn.close()
        return filasAfectadas
    
    def obtener_ultimo_id_insertado_socios(self):
        self.abrir_nueva_conexion()
        cursor = self.conn.cursor()
        cursor.execute("SELECT last_insert_rowid() FROM socios")
        resultado = cursor.fetchone()
        cursor.close()
        return resultado[0] if resultado else None
    
    def obtener_ultimo_id_insertado_libros(self):
        self.abrir_nueva_conexion()
        cursor = self.conn.cursor()
        cursor.execute("SELECT last_insert_rowid() FROM libros")
        resultado = cursor.fetchone()
        cursor.close()
        return resultado[0] if resultado else None
    
    def obtener_ultimo_id_insertado_prestamo(self):
        self.abrir_nueva_conexion()
        cursor = self.conn.cursor()
        cursor.execute("SELECT last_insert_rowid() FROM prestamos")
        resultado = cursor.fetchone()
        cursor.close()
        return resultado[0] if resultado else None
    
    def modif_tabla(self):
        self.abrir_nueva_conexion()
        cursor = self.conn.cursor()
        cursor.execute('ALTER TABLE socios ADD COLUMN borrado INTEGER')
    
    

    def crear_tablas(self):
        self.abrir_nueva_conexion()
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS libros (
            codigo INTEGER PRIMARY KEY AUTOINCREMENT, 
            titulo TEXT, 
            precioReposicion REAL, 
            estado TEXT,
            borrado INTEGER)''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS socios (
            numeroSocio INTEGER PRIMARY KEY AUTOINCREMENT, 
            nombre TEXT,
            borrado INTEGER)''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS prestamos (
            idPrestamo INTEGER PRIMARY KEY AUTOINCREMENT, 
            fechaPrestamo DATE, 
            diasDevolucion INTEGER, 
            diasRetraso INTEGER, 
            devuelto BOOLEAN, 
            socio_numeroSocio INTEGER, 
            libro_codigo INTEGER, 
            borrado INTEGER,
            diasRetrasoEnDevolucion INTEGER,
            FOREIGN KEY (socio_numeroSocio) REFERENCES socios (numeroSocio),
            FOREIGN KEY (libro_codigo) REFERENCES libros (codigo))''')
        trigger_sql = '''
        CREATE TRIGGER IF NOT EXISTS calcular_diasRetraso_insert_trigger
        AFTER INSERT ON prestamos
        FOR EACH ROW
        BEGIN
            UPDATE prestamos
            SET diasRetraso = CASE
                WHEN NEW.fechaPrestamo + NEW.diasDevolucion < CURRENT_DATE THEN 
                    CASE
                        WHEN CAST(CURRENT_DATE - (NEW.fechaPrestamo + NEW.diasDevolucion) AS INTEGER) < 0 THEN 0
                        ELSE CAST(CURRENT_DATE - (NEW.fechaPrestamo + NEW.diasDevolucion) AS INTEGER)
                    END
                ELSE
                    0  -- No hay retraso
                END
            WHERE idPrestamo = NEW.idPrestamo;
        END;
        '''
        trigger_sql1 = '''
        CREATE TRIGGER IF NOT EXISTS calcular_diasRetraso_update_trigger
        AFTER UPDATE ON prestamos
        FOR EACH ROW
        BEGIN
            UPDATE prestamos
                SET diasRetraso = CASE
                    WHEN NEW.fechaPrestamo + NEW.diasDevolucion < CURRENT_DATE THEN 
                        CASE
                            WHEN CAST(CURRENT_DATE - (NEW.fechaPrestamo + NEW.diasDevolucion) AS INTEGER) < 0 THEN 0
                            ELSE CAST(CURRENT_DATE - (NEW.fechaPrestamo + NEW.diasDevolucion) AS INTEGER)
                        END
                    ELSE
                        0  -- No hay retraso
                    END
            WHERE idPrestamo = NEW.idPrestamo;
        END;
        '''

        # Ejecutar el comando SQL para definir el trigger
        cursor.execute(trigger_sql)
        cursor.execute(trigger_sql1)
        self.conn.commit()
        cursor.close()
        
    