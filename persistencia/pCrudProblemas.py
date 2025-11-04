# Persistencia - pCrudProblemas.py
import sqlite3

class pCrudProblemas:
    def __init__(self, db_name="problemas.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.crear_tabla()

    def crear_tabla(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS problemas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descripcion TEXT UNIQUE,
                dificultad TEXT,
                lenguaje TEXT,
                aprobado INTEGER
            )
        """)
        self.conn.commit()

    def alta(self, problema):
        try:
            self.cursor.execute("""
                INSERT INTO problemas (descripcion, dificultad, lenguaje, aprobado)
                VALUES (?, ?, ?, ?)
            """, (problema.descripcion, problema.dificultad, problema.lenguaje, int(bool(problema.aprobado))))
            self.conn.commit()
            return True, "Problema agregado correctamente."
        except sqlite3.IntegrityError:
            return False, "Error: la descripción ya existe."

    def baja(self, descripcion):
        self.cursor.execute("DELETE FROM problemas WHERE descripcion = ?", (descripcion,))
        self.conn.commit()
        return self.cursor.rowcount > 0

    def modificar(self, descripcion, new_desc=None, new_dificultad=None, new_lenguaje=None, new_aprobado=None):
        campos = []
        valores = []

        if new_desc:
            campos.append("descripcion = ?")
            valores.append(new_desc)
        if new_dificultad:
            campos.append("dificultad = ?")
            valores.append(new_dificultad)
        if new_lenguaje:
            campos.append("lenguaje = ?")
            valores.append(new_lenguaje)
        if new_aprobado is not None:
            campos.append("aprobado = ?")
            valores.append(int(bool(new_aprobado)))

        if campos:
            valores.append(descripcion)
            consulta = f"UPDATE problemas SET {', '.join(campos)} WHERE descripcion = ?"
            self.cursor.execute(consulta, valores)
            self.conn.commit()
            return self.cursor.rowcount > 0
        return False

    def listar(self):
        self.cursor.execute("SELECT descripcion, dificultad, lenguaje, aprobado FROM problemas")
        rows = self.cursor.fetchall()
        return [(r[0], r[1], r[2], bool(r[3])) for r in rows]

    def ordenar_por_dificultad(self):
        self.cursor.execute("SELECT descripcion, dificultad, lenguaje, aprobado FROM problemas ORDER BY dificultad")
        rows = self.cursor.fetchall()
        return [(r[0], r[1], r[2], bool(r[3])) for r in rows]

    def cerrar_conexion(self):
        self.conn.close()
