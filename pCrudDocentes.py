import sqlite3

class CrudAlumnosSQLite:
    def __init__(self, db_name="alumnos.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.crear_tabla()

    def crear_tabla(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS alumnos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombreU TEXT,
                edad INTEGER,
                userA TEXT UNIQUE,
                passA TEXT
            )
        """)
        self.conn.commit()

    def alta(self, alumno):
        try:
            self.cursor.execute("""
                INSERT INTO alumnos (nombreU, edad, userA, passA)
                VALUES (?, ?, ?, ?)
            """, (alumno.nombreU, alumno.edad, alumno.userA, alumno.passA))
            self.conn.commit()
            print(f"Alumno '{alumno.userA}' agregado correctamente.")
        except sqlite3.IntegrityError:
            print(f"Error: el usuario '{alumno.userA}' ya existe.")

    def baja(self, userA):
        self.cursor.execute("DELETE FROM alumnos WHERE userA = ?", (userA,))
        self.conn.commit()
        if self.cursor.rowcount > 0:
            print(f"Alumno '{userA}' eliminado correctamente.")
        else:
            print(f"Alumno '{userA}' no encontrado.")

    def modificar(self, userA, new_nombreU=None, new_edad=None, new_userA=None, new_passA=None):
        campos = []
        valores = []

        if new_nombreU:
            campos.append("nombreU = ?")
            valores.append(new_nombreU)
        if new_edad:
            campos.append("edad = ?")
            valores.append(new_edad)
        if new_userA:
            campos.append("userA = ?")
            valores.append(new_userA)
        if new_passA:
            campos.append("passA = ?")
            valores.append(new_passA)

        if campos:
            valores.append(userA)
            consulta = f"UPDATE alumnos SET {', '.join(campos)} WHERE userA = ?"
            self.cursor.execute(consulta, valores)
            self.conn.commit()
            if self.cursor.rowcount > 0:
                print(f"Alumno '{userA}' modificado correctamente.")
            else:
                print(f"Alumno '{userA}' no encontrado.")
        else:
            print("No se proporcionaron datos para modificar.")

    def listar(self):
        self.cursor.execute("SELECT nombreU, edad, userA, passA FROM alumnos")
        alumnos = self.cursor.fetchall()
        if alumnos:
            for a in alumnos:
                print(f"Nombre: {a[0]}, Edad: {a[1]}, Usuario: {a[2]}, Contraseña: {a[3]}")
        else:
            print("No hay alumnos registrados.")

    def ordenar(self):
        self.cursor.execute("SELECT nombreU, edad, userA, passA FROM alumnos ORDER BY nombreU")
        alumnos = self.cursor.fetchall()
        for a in alumnos:
            print(f"Nombre: {a[0]}, Edad: {a[1]}, Usuario: {a[2]}, Contraseña: {a[3]}")

    def cerrar_conexion(self):
        self.conn.close()
