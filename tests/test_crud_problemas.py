#Aca aplican los mismos comentarios que en test_crud_alumnos.
import os
import tempfile
import pytest
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from persistencia.pCrudProblemas import pCrudProblemas
from logica.CrudProblemas import CrudProblemas
from logica.Problemas import Problemas

def test_crud_problemas_sqlite(tmp_path):
    db = tmp_path / "test_problemas.db"
    p = pCrudProblemas(db_name=str(db))
    c = CrudProblemas(pers=p)

    pr = Problemas("Suma", "Facil", "Python", True)
    ok, msg = c.alta(pr)
    assert ok is True

    rows = c.listar()
    assert any(r[0] == "Suma" for r in rows)

    ok, msg = c.modificar("Suma", new_desc="Suma v2", new_dificultad="Media", new_aprobado=False)
    assert ok is True
    rows = c.listar()
    assert any(r[0] == "Suma v2" and r[1] == "Media" and r[3] is False for r in rows)

    ok, msg = c.baja("Suma v2")
    assert ok is True
    rows = c.listar()
    assert not any(r[0] == "Suma v2" for r in rows)
