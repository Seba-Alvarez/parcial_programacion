import sqlite3

class CrudProblemasSQLite:
    def __init__(self, db_name="problemas.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.crear_tabla()

    def crear_tabla(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS problemas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descripcion TEXT,
                dificultad TEXT,
                lenguaje TEXT,
                aprobado BOOLEAN
            )
        """)
        self.conn.commit()

    def alta(self, problema):
        self.cursor.execute("""
            INSERT INTO problemas (descripcion, dificultad, lenguaje, aprobado)
            VALUES (?, ?, ?, ?)
        """, (problema.descripcion, problema.dificultad, problema.lenguaje, problema.aprobado))
        self.conn.commit()
        print("Problema agregado correctamente.")

    def baja(self, descripcion):
        self.cursor.execute("DELETE FROM problemas WHERE descripcion = ?", (descripcion,))
        self.conn.commit()
        print("Problema eliminado correctamente.")

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
            valores.append(new_aprobado)

        if campos:
            valores.append(descripcion)
            consulta = f"UPDATE problemas SET {', '.join(campos)} WHERE descripcion = ?"
            self.cursor.execute(consulta, valores)
            self.conn.commit()
            print("Problema modificado correctamente.")
        else:
            print("No se proporcionaron datos para modificar.")

    def listar(self):
        self.cursor.execute("SELECT descripcion, dificultad, lenguaje, aprobado FROM problemas")
        problemas = self.cursor.fetchall()
        for p in problemas:
            print(f"Descripción: {p[0]}, Dificultad: {p[1]}, Lenguaje: {p[2]}, Aprobado: {p[3]}")

    def ordenar_por_dificultad(self):
        self.cursor.execute("SELECT descripcion, dificultad, lenguaje, aprobado FROM problemas ORDER BY dificultad")
        problemas = self.cursor.fetchall()
        for p in problemas:
            print(f"Descripción: {p[0]}, Dificultad: {p[1]}, Lenguaje: {p[2]}, Aprobado: {p[3]}")

    def cerrar_conexion(self):
        self.conn.close()
