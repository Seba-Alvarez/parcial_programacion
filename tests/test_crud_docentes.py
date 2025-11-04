#Aca aplican los mismos comentarios que en test_crud_alumnos.
import os
import tempfile
import pytest
import pytest
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from persistencia.pCrudDocentes import pCrudDocentes
from logica.CrudDocentes import CrudDocentes
from logica.Docentes import Docentes

def test_crud_docentes_sqlite(tmp_path):
    db = tmp_path / "test_docentes.db"
    p = pCrudDocentes(db_name=str(db))
    c = CrudDocentes(pers=p)

    d1 = Docentes("Ana", 35, "anaT", "pwA")
    ok, msg = c.alta(d1)
    assert ok is True

    rows = c.listar()
    assert any(r[2] == "anaT" for r in rows)

    ok, msg = c.modificar("anaT", new_nombreU="Anita", new_edad=36, new_passD="pwB")
    assert ok is True
    rows = c.listar()
    assert any(r[0] == "Anita" and r[1] == 36 for r in rows)

    ok, msg = c.baja("anaT")
    assert ok is True
    rows = c.listar()
    assert not any(r[2] == "anaT" for r in rows)
