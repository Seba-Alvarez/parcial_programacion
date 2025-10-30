# Persistencia - pCrudDocentes.py
import sqlite3

class pCrudDocentes:
    """
    Persistencia SQLite para docentes.
    """
    def __init__(self, db_name="docentes.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.crear_tabla()

    def crear_tabla(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS docentes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombreU TEXT,
                edad INTEGER,
                userD TEXT UNIQUE,
                passD TEXT
            )
        """)
        self.conn.commit()

    def alta(self, docente):
        try:
            self.cursor.execute("""
                INSERT INTO docentes (nombreU, edad, userD, passD)
                VALUES (?, ?, ?, ?)
            """, (docente.nombreU, docente.edad, docente.userD, docente.passD))
            self.conn.commit()
            return True, f"Docente '{docente.userD}' agregado correctamente."
        except sqlite3.IntegrityError:
            return False, f"Error: el usuario '{docente.userD}' ya existe."

    def baja(self, userD):
        self.cursor.execute("DELETE FROM docentes WHERE userD = ?", (userD,))
        self.conn.commit()
        return self.cursor.rowcount > 0

    def modificar(self, userD, new_nombreU=None, new_edad=None, new_userD=None, new_passD=None):
        campos = []
        valores = []

        if new_nombreU:
            campos.append("nombreU = ?")
            valores.append(new_nombreU)
        if new_edad is not None:
            campos.append("edad = ?")
            valores.append(new_edad)
        if new_userD:
            campos.append("userD = ?")
            valores.append(new_userD)
        if new_passD:
            campos.append("passD = ?")
            valores.append(new_passD)

        if campos:
            valores.append(userD)
            consulta = f"UPDATE docentes SET {', '.join(campos)} WHERE userD = ?"
            self.cursor.execute(consulta, valores)
            self.conn.commit()
            return self.cursor.rowcount > 0
        return False

    def listar(self):
        self.cursor.execute("SELECT nombreU, edad, userD, passD FROM docentes")
        return self.cursor.fetchall()

    def ordenar(self):
        self.cursor.execute("SELECT nombreU, edad, userD, passD FROM docentes ORDER BY nombreU")
        return self.cursor.fetchall()

    def cerrar_conexion(self):
        self.conn.close()
