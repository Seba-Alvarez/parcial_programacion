class CrudDocentes:
    def __init__(self):
        self.docentes = []

    def alta(self, docente):
        self.docentes.append(docente)
        print(f"Docente '{docente.userD}' agregado correctamente.")

    def baja(self, userD):
        for docente in self.docentes:
            if docente.userD.lower() == userD.lower():
                self.docentes.remove(docente)
                print(f"Docente '{userD}' eliminado correctamente.")
                return
        print(f"Docente '{userD}' no encontrado.")

    def modificar(self, userD, new_nombreU=None, new_edad=None, new_userD=None, new_passD=None):
        for docente in self.docentes:
            if docente.userD.lower() == userD.lower():
                if new_nombreU:
                    docente.set_nombreU(new_nombreU)
                if new_edad:
                    docente.set_edad(new_edad)
                if new_userD:
                    docente.set_userD(new_userD)
                if new_passD:
                    docente.set_passD(new_passD)
                print(f"Docente '{userD}' modificado correctamente.")
                return
        print(f"Docente '{userD}' no encontrado.")

    def listar(self):
        if not self.docentes:
            print("No hay docentes registrados.")
        else:
            for docente in self.docentes:
                print(docente)

    def ordenar(self):
        self.docentes.sort(key=lambda docente: docente.nombreU)
        print("Docentes ordenados por nombre.")
