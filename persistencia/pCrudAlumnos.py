# Persistencia - pCrudAlumnos.py
import sqlite3

class pCrudAlumnos:
    """
    Persistencia SQLite para alumnos.
    """
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
            return True, f"Alumno '{alumno.userA}' agregado correctamente."
        except sqlite3.IntegrityError:
            return False, f"Error: el usuario '{alumno.userA}' ya existe."

    def baja(self, userA):
        self.cursor.execute("DELETE FROM alumnos WHERE userA = ?", (userA,))
        self.conn.commit()
        return self.cursor.rowcount > 0

    def modificar(self, userA, new_nombreU=None, new_edad=None, new_userA=None, new_passA=None):
        campos = []
        valores = []

        if new_nombreU:
            campos.append("nombreU = ?")
            valores.append(new_nombreU)
        if new_edad is not None:
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
            return self.cursor.rowcount > 0
        return False

    def listar(self):
        self.cursor.execute("SELECT nombreU, edad, userA, passA FROM alumnos")
        return self.cursor.fetchall()

    def ordenar(self):
        self.cursor.execute("SELECT nombreU, edad, userA, passA FROM alumnos ORDER BY nombreU")
        return self.cursor.fetchall()

    def cerrar_conexion(self):
        self.conn.close()
