import os
import sqlite3
import pytest
from server.database import get_db_connection, init_db, crear_usuario, obtener_usuario_por_nombre
from server.auth import hash_password

@pytest.fixture
def test_db(tmp_path):
    """Fixture que proporciona la ruta a una base de datos SQLite temporal."""
    db_file = tmp_path / "test_tareas.db"
    db_path = str(db_file)
    init_db(db_path)
    return db_path

def test_init_db_crea_tablas(test_db):
    conn = get_db_connection(test_db)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row['name'] for row in cursor.fetchall()]
    conn.close()

    assert "usuarios" in tables
    assert "tareas" in tables

def test_crear_y_obtener_usuario(test_db):
    pwd_hash = hash_password("secret123")
    user_id = crear_usuario("usuario_test", pwd_hash, db_path=test_db)
    
    assert user_id is not None
    assert user_id > 0

    usuario = obtener_usuario_por_nombre("usuario_test", db_path=test_db)
    assert usuario is not None
    assert usuario['usuario'] == "usuario_test"
    assert usuario['contrasena_hash'] == pwd_hash

def test_usuario_duplicado_lanza_excepcion(test_db):
    pwd_hash = hash_password("secret123")
    crear_usuario("duplicado", pwd_hash, db_path=test_db)

    with pytest.raises(sqlite3.IntegrityError):
        crear_usuario("duplicado", pwd_hash, db_path=test_db)

def test_obtener_usuario_inexistente(test_db):
    usuario = obtener_usuario_por_nombre("fantasma", db_path=test_db)
    assert usuario is None
