# Lógica - CrudDocentes.py
from .Docentes import Docentes

class CrudDocentes:
    def __init__(self, pers=None):
        self.docentes = []
        self.pers = pers

    def alta(self, docente):
        if self.pers:
            ok, msg = self.pers.alta(docente)
            return ok, msg
        self.docentes.append(docente)
        return True, f"Docente '{docente.userD}' agregado correctamente."

    def baja(self, userD):
        if self.pers:
            ok = self.pers.baja(userD)
            return ok, ("Eliminado" if ok else "No encontrado")
        for docente in self.docentes:
            if docente.userD.lower() == userD.lower():
                self.docentes.remove(docente)
                return True, f"Docente '{userD}' eliminado correctamente."
        return False, f"Docente '{userD}' no encontrado."

    def modificar(self, userD, new_nombreU=None, new_edad=None, new_userD=None, new_passD=None):
        if self.pers:
            ok = self.pers.modificar(userD, new_nombreU=new_nombreU, new_edad=new_edad, new_userD=new_userD, new_passD=new_passD)
            return ok, ("Modificado" if ok else "No encontrado")
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
                return True, f"Docente '{userD}' modificado correctamente."
        return False, f"Docente '{userD}' no encontrado."

    def listar(self):
        if self.pers:
            return self.pers.listar()
        return [str(d) for d in self.docentes]

    def ordenar(self):
        if self.pers:
            return self.pers.ordenar()
        self.docentes.sort(key=lambda docente: docente.nombreU)
        return [str(d) for d in self.docentes]
