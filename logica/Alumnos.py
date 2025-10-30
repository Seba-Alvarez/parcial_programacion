# Lógica - Alumnos.py
from .Usuarios import Usuarios

class Alumnos(Usuarios):
    def __init__(self, nombreU, edad, userA, passA):
        super().__init__(nombreU, edad)
        self.userA = userA
        self.passA = passA

    # Getters
    def get_userA(self):
        return self.userA

    def get_passA(self):
        return self.passA

    # Setters
    def set_userA(self, userA):
        self.userA = userA

    def set_passA(self, passA):
        self.passA = passA

    def __str__(self):
        return f"[Alumno] Nombre: {self.nombreU}, Edad: {self.edad}, Usuario: {self.userA}"
