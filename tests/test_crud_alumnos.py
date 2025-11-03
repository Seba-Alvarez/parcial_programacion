#se importan las librerias para hacer los testeos
#os para el pathing
import os
#tempfile para las pruebas con archivos mock
import tempfile
#pytest para hacer el testeo como tal
import pytest
#sys tambien para el pathing
import sys

#esto permite importar módulos de carpetas superiores (logica, persistencia) sin errores
#cortesía de chatgpt porque no lo podia hacer andar a los testeos
#fue lo ultimo que hicimos del codigo
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#se importan las clases que se necesitan para el test
from persistencia.pCrudAlumnos import pCrudAlumnos
from logica.CrudAlumnos import CrudAlumnos
from logica.Alumnos import Alumnos

#fundamental que empiece con test_ porque sino no anda
def test_crud_alumnos_sqlite(tmp_path):
    #define la ruta para la base de datos temporal.
    db = tmp_path / "test_alumnos.db"
    #crea la instancia de persistencia usando la db temporal (lo de arriba).
    p = pCrudAlumnos(db_name=str(db))
    #crea la instancia del crud, vinculada a la persistencia.
    c = CrudAlumnos(pers=p)

    #testeando el alta
    a1 = Alumnos("Juan", 20, "juan123", "pw1")
    ok, msg = c.alta(a1)
    assert ok is True

    #testeando el listar
    rows = c.listar()
    assert any(r[2] == "juan123" for r in rows)

    #testeando el modificar
    ok, msg = c.modificar("juan123", new_nombreU="Juanito", new_edad=21, new_passA="pw2")
    assert ok is True
    
    #otra vez el listar, pero despues del modificar
    rows = c.listar()
    assert any(r[0] == "Juanito" and r[1] == 21 for r in rows)

    #testeando el baja
    ok, msg = c.baja("juan123")
    assert ok is True

    #una ultima vez
    rows = c.listar()
    #este es el mas importante en realidad
    #porque despues de las operaciones (la ultima fue eliminar)
    #no tendria que estar el alumno en la db
    assert not any(r[2] == "juan123" for r in rows)
