# Lógica - CrudProblemas.py
from .Problemas import Problemas

class CrudProblemas:
    def __init__(self, pers=None):
        self.problemas = []
        self.pers = pers

    def alta(self, problema):
        if self.pers:
            ok, msg = self.pers.alta(problema)
            return ok, msg
        self.problemas.append(problema)
        return True, "Problema agregado correctamente."

    def baja(self, descripcion):
        if self.pers:
            ok = self.pers.baja(descripcion)
            return ok, ("Eliminado" if ok else "No encontrado")
        for problema in self.problemas:
            if problema.descripcion.lower() == descripcion.lower():
                self.problemas.remove(problema)
                return True, f"Problema '{descripcion}' eliminado correctamente."
        return False, f"Problema '{descripcion}' no encontrado."

    def modificar(self, descripcion, new_desc=None, new_dificultad=None, new_lenguaje=None, new_aprobado=None):
        if self.pers:
            ok = self.pers.modificar(descripcion, new_desc=new_desc, new_dificultad=new_dificultad, new_lenguaje=new_lenguaje, new_aprobado=new_aprobado)
            return ok, ("Modificado" if ok else "No encontrado")
        for problema in self.problemas:
            if problema.descripcion.lower() == descripcion.lower():
                if new_desc:
                    problema.set_descripcion(new_desc)
                if new_dificultad:
                    problema.set_dificultad(new_dificultad)
                if new_lenguaje:
                    problema.set_lenguaje(new_lenguaje)
                if new_aprobado is not None:
                    problema.set_aprobado(new_aprobado)
                return True, f"Problema '{descripcion}' modificado correctamente."
        return False, f"Problema '{descripcion}' no encontrado."

    def listar(self):
        if self.pers:
            return self.pers.listar()
        return [str(p) for p in self.problemas]

    def ordenar(self):
        if self.pers:
            return self.pers.ordenar_por_dificultad()
        self.problemas.sort(key=lambda problema: problema.dificultad)
        return [str(p) for p in self.problemas]
