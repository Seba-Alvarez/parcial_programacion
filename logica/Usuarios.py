class Usuarios:
    def __init__(self, nombreU, edad):
        self.nombreU = nombreU
        self.edad = edad

    def get_nombreU(self):
        return self.nombreU

    def get_edad(self):
        return self.edad

    def set_nombreU(self, nombreU):
        self.nombreU = nombreU

    def set_edad(self, edad):
        self.edad = edad
