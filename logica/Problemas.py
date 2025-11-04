#Aca aplican los mismos comentarios que en Alumnos, con la salvedad que Problemas no esta heredando.
class Problemas:
    def __init__(self, descripcion, dificultad, lenguaje, aprobado):
        self.descripcion = descripcion
        self.dificultad = dificultad
        self.lenguaje = lenguaje
        self.aprobado = aprobado

    # Getters
    def get_descripcion(self):
        return self.descripcion

    def get_dificultad(self):
        return self.dificultad

    def get_lenguaje(self):
        return self.lenguaje

    def get_aprobado(self):
        return self.aprobado

    # Setters
    def set_descripcion(self, descripcion):
        self.descripcion = descripcion

    def set_dificultad(self, dificultad):
        self.dificultad = dificultad

    def set_lenguaje(self, lenguaje):
        self.lenguaje = lenguaje

    def set_aprobado(self, aprobado):
        self.aprobado = aprobado

    def __str__(self):
        return f"[Problema] Descripción: {self.descripcion}, Dificultad: {self.dificultad}, Lenguaje: {self.lenguaje}, Aprobado: {self.aprobado}"
