#importamos el todopoderoso eseculaite
#hubiera sido mas facil usar sql comun....
import sqlite3

#esta clase maneja el crud de alumnos en la persistencia
class pCrudAlumnos:
    #se abre una base de datos SQLite con el nombre db_name, 
    #si no existe, SQLite la crea automáticamente con el nombre "alumnos"
    #es mas facil hacer 3 bases de datos separadas que una sola con todo
    #porque técnicamente no es una base de datos relacional per se
    def __init__(self, db_name="alumnos.db"):
        #se concecta con la "base de datos"
        self.conn = sqlite3.connect(db_name)
        #crea un cursor, que sirve para ejecutar consultas
        #un cursor es un objeto que hace de intermediario entre python y la db 
        self.cursor = self.conn.cursor()
        #se crea la tabla por si no existiese
        self.crear_tabla()

    #este es el create table, este se ejecuta una sola ves
    #a menos que se borre la base de datos
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
        #aca se confirma los cambios en la base de datos.
        self.conn.commit()

    #para agregar alumnos a la db
    #? son placeholders, que previenen inyecciones directas en sql
    #en su lugar se ejecutan a traves de python
    def alta(self, alumno):
        try:
            self.cursor.execute("""
                INSERT INTO alumnos (nombreU, edad, userA, passA)
                VALUES (?, ?, ?, ?)
            """, (alumno.nombreU, alumno.edad, alumno.userA, alumno.passA))
            #si nada se partio hace los inserts
            self.conn.commit()
            return True, f"Alumno '{alumno.userA}' agregado correctamente."
        except sqlite3.IntegrityError:
            #Si el userA ya existe, tira error y devuelve un mensaje.
            return False, f"Error: el usuario '{alumno.userA}' ya existe."

    #bien simple, se le pasa un user por parametro y lo borra
    def baja(self, userA):
        #la consulta sql con el placeholder para pasarle el dato por python no por sql
        self.cursor.execute("DELETE FROM alumnos WHERE userA = ?", (userA,))
        #hace los cambios
        self.conn.commit()
        #significa que se eliminó al menos un alumno, y devuelve true
        #esto habría que mejorarlo a futuro con una busqueda mas exaustiva, pero por ahora funciona
        return self.cursor.rowcount > 0

    #Se arma la sentencia SQL para modificar solo los campos que se pasen, para evitar NULL
    #campos es una lista de columnas a modificar con placeholders ?.
    #valores es una lista de valores para la ejecución (nunca está de mas usar mas de una lista por seguridad).
    def modificar(self, userA, new_nombreU=None, new_edad=None, new_userA=None, new_passA=None):
        campos = []
        valores = []

        #si se le pasaron nuevos valores, guarda los datos primero como placeholder
        #y despues guarda el valor en si mismo
        if new_nombreU:
            campos.append("nombreU = ?")
            valores.append(new_nombreU)
        #lo mismo que arriba
        if new_edad is not None:
            campos.append("edad = ?")
            valores.append(new_edad)
        #x2
        if new_userA:
            campos.append("userA = ?")
            valores.append(new_userA)
        #x3
        if new_passA:
            campos.append("passA = ?")
            valores.append(new_passA)

        #Si hay campos para actualizar, se añade userA al final de valores para usarlo en el WHERE
        if campos:
            valores.append(userA)
            #esto fue horrible, insisto, es mas simple hacer una base de datos en sql
            consulta = f"UPDATE alumnos SET {', '.join(campos)} WHERE userA = ?"
            #Ejecuta la consulta y hace commit().
            self.cursor.execute(consulta, valores)
            self.conn.commit()
            #lo mismo que con el borrar, algo a mejorar
            return self.cursor.rowcount > 0
        #Si no hay campos nuevos, no hay nada para actualizar.
        return False

    #un simple listar
    def listar(self):
        #consulta sql
        self.cursor.execute("SELECT nombreU, edad, userA, passA FROM alumnos")
        #fetchall trae una lista de tuplas
        return self.cursor.fetchall()

    #igual que arriba pero con listar
    def ordenar(self):
        self.cursor.execute("SELECT nombreU, edad, userA, passA FROM alumnos ORDER BY nombreU")
        return self.cursor.fetchall()

    #se cierra la conexión para que solo este corriendo mientras está en uso
    def cerrar_conexion(self):
        self.conn.close()
