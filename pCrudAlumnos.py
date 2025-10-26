import sqlite3

class CrudDocentesSQLite:
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
            print(f"Docente '{docente.userD}' agregado correctamente.")
        except sqlite3.IntegrityError:
            print(f"Error: el usuario '{docente.userD}' ya existe.")

    def baja(self, userD):
        self.cursor.execute("DELETE FROM docentes WHERE userD = ?", (userD,))
        self.conn.commit()
        if self.cursor.rowcount > 0:
            print(f"Docente '{userD}' eliminado correctamente.")
        else:
            print(f"Docente '{userD}' no encontrado.")

    def modificar(self, userD, new_nombreU=None, new_edad=None, new_userD=None, new_passD=None):
        campos = []
        valores = []

        if new_nombreU:
            campos.append("nombreU = ?")
            valores.append(new_nombreU)
        if new_edad:
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
            if self.cursor.rowcount > 0:
                print(f"Docente '{userD}' modificado correctamente.")
            else:
                print(f"Docente '{userD}' no encontrado.")
        else:
            print("No se proporcionaron datos para modificar.")

    def listar(self):
        self.cursor.execute("SELECT nombreU, edad, userD, passD FROM docentes")
        docentes = self.cursor.fetchall()
        if docentes:
            for d in docentes:
                print(f"Nombre: {d[0]}, Edad: {d[1]}, Usuario: {d[2]}, Contraseña: {d[3]}")
        else:
            print("No hay docentes registrados.")

    def ordenar(self):
        self.cursor.execute("SELECT nombreU, edad, userD, passD FROM docentes ORDER BY nombreU")
        docentes = self.cursor.fetchall()
        for d in docentes:
            print(f"Nombre: {d[0]}, Edad: {d[1]}, Usuario: {d[2]}, Contraseña: {d[3]}")

    def cerrar_conexion(self):
        self.conn.close()
