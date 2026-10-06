import pytest
import json
from server.servidor import create_app
from server.database import obtener_usuario_por_nombre

@pytest.fixture
def client(tmp_path):
    db_file = tmp_path / "test_api_tareas.db"
    db_path = str(db_file)
    app = create_app(db_path=db_path)
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_endpoint(client):
    rv = client.get('/')
    assert rv.status_code == 200
    data = rv.get_json()
    assert "API REST" in data['nombre']

def test_registro_exitoso(client):
    payload = {
        "usuario": "carlos",
        "contraseña": "claveSegura123"
    }
    rv = client.post('/registro', json=payload)
    assert rv.status_code == 201
    data = rv.get_json()
    assert data['mensaje'] == "Usuario registrado exitosamente"
    assert data['usuario'] == "carlos"

def test_registro_campos_faltantes(client):
    payload = {"usuario": "carlos"}
    rv = client.post('/registro', json=payload)
    assert rv.status_code == 400
    data = rv.get_json()
    assert "error" in data

def test_registro_usuario_duplicado(client):
    payload = {
        "usuario": "ana",
        "contraseña": "1234"
    }
    rv1 = client.post('/registro', json=payload)
    assert rv1.status_code == 201

    rv2 = client.post('/registro', json=payload)
    assert rv2.status_code == 409
    data = rv2.get_json()
    assert "El usuario ya existe" in data['error']

def test_login_exitoso(client):
    # Registrar primero
    reg_payload = {"usuario": "maria", "contraseña": "miPassword"}
    client.post('/registro', json=reg_payload)

    # Iniciar sesión
    login_payload = {"usuario": "maria", "contraseña": "miPassword"}
    rv = client.post('/login', json=login_payload)
    assert rv.status_code == 200
    data = rv.get_json()
    assert data['mensaje'] == "Inicio de sesión exitoso"
    assert data['usuario'] == "maria"

def test_login_contrasena_incorrecta(client):
    reg_payload = {"usuario": "pedro", "contraseña": "correcta"}
    client.post('/registro', json=reg_payload)

    login_payload = {"usuario": "pedro", "contraseña": "incorrecta"}
    rv = client.post('/login', json=login_payload)
    assert rv.status_code == 401
    data = rv.get_json()
    assert data['error'] == "Credenciales inválidas"

def test_login_usuario_inexistente(client):
    login_payload = {"usuario": "no_existo", "contraseña": "1234"}
    rv = client.post('/login', json=login_payload)
    assert rv.status_code == 401
    data = rv.get_json()
    assert data['error'] == "Credenciales inválidas"

def test_tareas_endpoint_retorna_html(client):
    rv = client.get('/tareas')
    assert rv.status_code == 200
    assert rv.content_type.startswith("text/html")
    html_text = rv.get_data(as_text=True)
    assert "¡Bienvenido al Sistema de Gestión de Tareas!" in html_text
    assert "PFO 2" in html_text
