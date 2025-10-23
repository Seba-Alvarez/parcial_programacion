class CrudAlumnos:
    def __init__(self):
        self.alumnos = []

    def alta(self, alumno):
        self.alumnos.append(alumno)
        print(f"Alumno '{alumno.userA}' agregado correctamente.")

    def baja(self, userA):
        for alumno in self.alumnos:
            if alumno.userA.lower() == userA.lower():
                self.alumnos.remove(alumno)
                print(f"Alumno '{userA}' eliminado correctamente.")
                return
        print(f"Alumno '{userA}' no encontrado.")

    def modificar(self, userA, new_nombreU=None, new_edad=None, new_userA=None, new_passA=None):
        for alumno in self.alumnos:
            if alumno.userA.lower() == userA.lower():
                if new_nombreU:
                    alumno.set_nombreU(new_nombreU)
                if new_edad:
                    alumno.set_edad(new_edad)
                if new_userA:
                    alumno.set_userA(new_userA)
                if new_passA:
                    alumno.set_passA(new_passA)
                print(f"Alumno '{userA}' modificado correctamente.")
                return
        print(f"Alumno '{userA}' no encontrado.")

    def listar(self):
        if not self.alumnos:
            print("No hay alumnos registrados.")
        else:
            for alumno in self.alumnos:
                print(alumno)

    def ordenar(self):
        self.alumnos.sort(key=lambda alumno: alumno.nombreU)
        print("Alumnos ordenados por nombre.")
