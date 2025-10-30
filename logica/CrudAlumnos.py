# Lógica - CrudAlumnos.py
from .Alumnos import Alumnos

class CrudAlumnos:
    def __init__(self, pers=None):
        """
        pers: instancia de persistencia (pCrudAlumnos) opcional.
        Si se pasa, la mayoría de las operaciones delegan a la persistencia.
        """
        self.alumnos = []
        self.pers = pers

    def alta(self, alumno):
        if self.pers:
            ok, msg = self.pers.alta(alumno)
            return ok, msg
        self.alumnos.append(alumno)
        return True, f"Alumno '{alumno.userA}' agregado correctamente."

    def baja(self, userA):
        if self.pers:
            ok = self.pers.baja(userA)
            return ok, ("Eliminado" if ok else "No encontrado")
        for alumno in self.alumnos:
            if alumno.userA.lower() == userA.lower():
                self.alumnos.remove(alumno)
                return True, f"Alumno '{userA}' eliminado correctamente."
        return False, f"Alumno '{userA}' no encontrado."

    def modificar(self, userA, new_nombreU=None, new_edad=None, new_userA=None, new_passA=None):
        if self.pers:
            ok = self.pers.modificar(userA, new_nombreU=new_nombreU, new_edad=new_edad, new_userA=new_userA, new_passA=new_passA)
            return ok, ("Modificado" if ok else "No encontrado")
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
                return True, f"Alumno '{userA}' modificado correctamente."
        return False, f"Alumno '{userA}' no encontrado."

    def listar(self):
        if self.pers:
            return self.pers.listar()
        return [str(a) for a in self.alumnos]

    def ordenar(self):
        if self.pers:
            return self.pers.ordenar()
        self.alumnos.sort(key=lambda alumno: alumno.nombreU)
        return [str(a) for a in self.alumnos]
