class CrudProblemas:
    def __init__(self):
        self.problemas = []

    def alta(self, problema):
        self.problemas.append(problema)
        print(f"Problema '{problema.descripcion}' agregado correctamente.")

    def baja(self, descripcion):
        for problema in self.problemas:
            if problema.descripcion.lower() == descripcion.lower():
                self.problemas.remove(problema)
                print(f"Problema '{descripcion}' eliminado correctamente.")
                return
        print(f"Problema '{descripcion}' no encontrado.")

    def modificar(self, descripcion, new_desc=None, new_dificultad=None, new_lenguaje=None, new_aprobado=None):
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
                print(f"Problema '{descripcion}' modificado correctamente.")
                return
        print(f"Problema '{descripcion}' no encontrado.")

    def listar(self):
        if not self.problemas:
            print("No hay problemas registrados.")
        else:
            for problema in self.problemas:
                print(problema)

    def ordenar(self):
        self.problemas.sort(key=lambda problema: problema.dificultad)
        print("Problemas ordenados por dificultad.")
