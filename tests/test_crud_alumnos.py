import os
import tempfile
import pytest
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from persistencia.pCrudAlumnos import pCrudAlumnos
from logica.CrudAlumnos import CrudAlumnos
from logica.Alumnos import Alumnos

def test_crud_alumnos_sqlite(tmp_path):
    db = tmp_path / "test_alumnos.db"
    p = pCrudAlumnos(db_name=str(db))
    c = CrudAlumnos(pers=p)

    a1 = Alumnos("Juan", 20, "juan123", "pw1")
    ok, msg = c.alta(a1)
    assert ok is True

    rows = c.listar()
    assert any(r[2] == "juan123" for r in rows)

    ok, msg = c.modificar("juan123", new_nombreU="Juanito", new_edad=21, new_passA="pw2")
    assert ok is True
    rows = c.listar()
    assert any(r[0] == "Juanito" and r[1] == 21 for r in rows)

    ok, msg = c.baja("juan123")
    assert ok is True
    rows = c.listar()
    assert not any(r[2] == "juan123" for r in rows)
