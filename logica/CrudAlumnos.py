#se importan los atributos de la clase Alumnos, el . significa que es un modulo relativo
#esto es para no harcodear los paths con os, ya tuvimos problemas con eso
from .Alumnos import Alumnos

class CrudAlumnos:
    def __init__(self, pers=None):
        #lista de alumnos para guardar los datos y manejarlos con la persistencia
        self.alumnos = []
        #pers: instancia de persistencia (pCrudAlumnos).
        self.pers = pers

    #
    def alta(self, alumno):
        #si la persistencia existe
        if self.pers:
            #se delega el alta como tal a la persistencia
            ok, msg = self.pers.alta(alumno)
            #se da el ok
            return ok, msg
        #aca se agregan los datos del alumno
        #se estan guardando en local (en la lista) y en la persistencia
        self.alumnos.append(alumno)
        #aca se chequea si se retorna true, se agregó correctamente
        return True, f"Alumno '{alumno.userA}' agregado correctamente."

    #lo mismo que con el alta
    def baja(self, userA):
        #se chequea si hay persistencia
        if self.pers:
            #esto va por el lado de la persistencia
            ok = self.pers.baja(userA)
            return ok, ("Eliminado" if ok else "No encontrado")
        #tecnicamente remove solo quita la primera ocurrencia
        #pero como se busca por usuario (un unique) esto no importa
        for alumno in self.alumnos:
            #si los usuarios (el seleccionado) y el de la lista de esta clase coinciden
            if alumno.userA.lower() == userA.lower():
                #se quita el alumno de la lista
                self.alumnos.remove(alumno)
                #mensaje explicando que no se rompio nada
                return True, f"Alumno '{userA}' eliminado correctamente."
        #por si algo male sal
        return False, f"Alumno '{userA}' no encontrado."

    #aca se modifican los alumnos
    #dos cosas, primero, se inicialisan los valores como new_valor=none para ingresar los nuevos valores
    #segudo, esto es igual que los otros dos metodos en el sentido que la primera parte
    #"delega" a la persistencia y la segunda lo hace en local
    def modificar(self, userA, new_nombreU=None, new_edad=None, new_userA=None, new_passA=None):
        #esto es lo de la persistencia
        if self.pers:
            ok = self.pers.modificar(userA, new_nombreU=new_nombreU, new_edad=new_edad, new_userA=new_userA, new_passA=new_passA)
            return ok, ("Modificado" if ok else "No encontrado")
        #aca es en local
        #si existen alumnos
        for alumno in self.alumnos:
            #si hay coincidencias con el alumno en cuestión
            #.lower es para que ponga todo en minuscula
            #para evitar cosas como Luis y luis sean diferentes
            if alumno.userA.lower() == userA.lower():
                #se asignan los nuevos valores
                if new_nombreU:
                    alumno.set_nombreU(new_nombreU)
                if new_edad:
                    alumno.set_edad(new_edad)
                if new_userA:
                    alumno.set_userA(new_userA)
                if new_passA:
                    alumno.set_passA(new_passA)
                #mensaje de congratulaciones
                return True, f"Alumno '{userA}' modificado correctamente."
        #mensaje de game over
        return False, f"Alumno '{userA}' no encontrado."

    #este listar, tambien llama primero al listar de la  persistencia
    def listar(self):
        #aca
        if self.pers:
            return self.pers.listar()
        #aca recorre la lista de esta clase
        return [str(a) for a in self.alumnos]

    #nuevamente, primero la persistencia y luego en local
    def ordenar(self):
        if self.pers:
            return self.pers.ordenar()
        #aca se estan ordenando por orden alfabetico, concretamente por nombre de usuario
        self.alumnos.sort(key=lambda alumno: alumno.nombreU)
        return [str(a) for a in self.alumnos]
