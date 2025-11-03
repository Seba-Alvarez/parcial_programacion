#Como esta heredando de usuarios, hay que importarlo
from .Usuarios import Usuarios

#clase Alumnos y su clase padre
class Alumnos(Usuarios):
    #constrictor con los datos de la clase (y los del padre)
    def __init__(self, nombreU, edad, userA, passA):
        #super para heredar los atributos
        super().__init__(nombreU, edad)
        #estos son unicos de de Alumnos
        self.userA = userA
        self.passA = passA

    #atributos privados encapsulados:
    
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

    #se define cómo se muestra un objeto Alumnos, en este caso como string
    def __str__(self):
        return f"[Alumno] Nombre: {self.nombreU}, Edad: {self.edad}, Usuario: {self.userA}"
