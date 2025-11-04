#Aca aplican los mismos comentarios que en Alumnos.
from .Usuarios import Usuarios

class Docentes(Usuarios):
    def __init__(self, nombreU, edad, userD, passD):
        super().__init__(nombreU, edad)
        self.userD = userD
        self.passD = passD

    # Getters
    def get_userD(self):
        return self.userD

    def get_passD(self):
        return self.passD

    # Setters
    def set_userD(self, userD):
        self.userD = userD

    def set_passD(self, passD):
        self.passD = passD

    def __str__(self):
        return f"[Docente] Nombre: {self.nombreU}, Edad: {self.edad}, Usuario: {self.userD}"
