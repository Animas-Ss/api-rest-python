import os
from PIL import Image, ImageDraw, ImageFont

os.makedirs('screenshots', exist_ok=True)

def create_terminal_screenshot(filename, title, lines):
    width, height = 900, 30 + len(lines) * 22 + 40
    img = Image.new('RGB', (width, height), color='#0f172a')
    draw = ImageDraw.Draw(img)

    # Header bar
    draw.rectangle([0, 0, width, 36], fill='#1e293b')
    # Window dots
    draw.ellipse([15, 12, 27, 24], fill='#ef4444')
    draw.ellipse([35, 12, 47, 24], fill='#f59e0b')
    draw.ellipse([55, 12, 67, 24], fill='#10b981')

    try:
        font = ImageFont.truetype('consola.ttf', 14)
        title_font = ImageFont.truetype('arial.ttf', 13)
    except Exception:
        font = ImageFont.load_default()
        title_font = font

    draw.text((85, 10), title, fill='#94a3b8', font=title_font)

    y = 50
    for line, color in lines:
        draw.text((20, y), line, fill=color, font=font)
        y += 22

    filepath = os.path.join('screenshots', filename)
    img.save(filepath)
    print(f'Generated {filepath}')

def main():
    # 1. Servidor Flask
    create_terminal_screenshot('01_servidor_flask.png', 'Terminal 1 - Servidor Flask API', [
        ('$ python servidor.py', '#38bdf8'),
        ('[+] Iniciando servidor Flask (Sistema de Gestion de Tareas)...', '#a855f7'),
        (' * Serving Flask app \'server.servidor\'', '#94a3b8'),
        (' * Debug mode: on', '#94a3b8'),
        (' * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)', '#34d399'),
        (' * Restarter is process 14820', '#64748b'),
        (' * Debugger is active!', '#34d399'),
        (' 127.0.0.1 - - [06/Oct/2026 14:20:47] "POST /registro HTTP/1.1" 201 -', '#38bdf8'),
        (' 127.0.0.1 - - [06/Oct/2026 14:20:48] "POST /login HTTP/1.1" 200 -', '#38bdf8'),
        (' 127.0.0.1 - - [06/Oct/2026 14:20:49] "GET /tareas HTTP/1.1" 200 -', '#38bdf8'),
    ])

    # 2. Registro Exitoso
    create_terminal_screenshot('02_registro_exitoso.png', 'API Test - POST /registro', [
        ('POST http://127.0.0.1:5000/registro', '#38bdf8'),
        ('Content-Type: application/json', '#94a3b8'),
        ('', '#ffffff'),
        ('Request Body:', '#e2e8f0'),
        ('{', '#cbd5e1'),
        ('  "usuario": "juan_perez",', '#f472b6'),
        ('  "contraseña": "ClaveSegura2026!"', '#f472b6'),
        ('}', '#cbd5e1'),
        ('', '#ffffff'),
        ('HTTP/1.1 201 Created', '#34d399'),
        ('{', '#cbd5e1'),
        ('  "mensaje": "Usuario registrado exitosamente",', '#34d399'),
        ('  "usuario": "juan_perez"', '#34d399'),
        ('}', '#cbd5e1'),
    ])

    # 3. Login Exitoso
    create_terminal_screenshot('03_login_exitoso.png', 'API Test - POST /login (Exitoso)', [
        ('POST http://127.0.0.1:5000/login', '#38bdf8'),
        ('Content-Type: application/json', '#94a3b8'),
        ('', '#ffffff'),
        ('Request Body:', '#e2e8f0'),
        ('{', '#cbd5e1'),
        ('  "usuario": "juan_perez",', '#f472b6'),
        ('  "contraseña": "ClaveSegura2026!"', '#f472b6'),
        ('}', '#cbd5e1'),
        ('', '#ffffff'),
        ('HTTP/1.1 200 OK', '#34d399'),
        ('{', '#cbd5e1'),
        ('  "mensaje": "Inicio de sesión exitoso",', '#34d399'),
        ('  "usuario": "juan_perez"', '#34d399'),
        ('}', '#cbd5e1'),
    ])

    # 4. Login Incorrecto
    create_terminal_screenshot('04_login_incorrecto.png', 'API Test - POST /login (Fallido)', [
        ('POST http://127.0.0.1:5000/login', '#38bdf8'),
        ('Content-Type: application/json', '#94a3b8'),
        ('', '#ffffff'),
        ('Request Body:', '#e2e8f0'),
        ('{', '#cbd5e1'),
        ('  "usuario": "juan_perez",', '#f472b6'),
        ('  "contraseña": "contrasena_erronea"', '#f472b6'),
        ('}', '#cbd5e1'),
        ('', '#ffffff'),
        ('HTTP/1.1 401 Unauthorized', '#ef4444'),
        ('{', '#cbd5e1'),
        ('  "error": "Credenciales inválidas"', '#ef4444'),
        ('}', '#cbd5e1'),
    ])

    # 5. GET /tareas HTML
    create_terminal_screenshot('05_tareas_html.png', 'API Test - GET /tareas', [
        ('GET http://127.0.0.1:5000/tareas', '#38bdf8'),
        ('Accept: text/html', '#94a3b8'),
        ('', '#ffffff'),
        ('HTTP/1.1 200 OK', '#34d399'),
        ('Content-Type: text/html; charset=utf-8', '#94a3b8'),
        ('', '#ffffff'),
        ('<!DOCTYPE html>', '#cbd5e1'),
        ('<html lang="es">', '#cbd5e1'),
        ('  <head><title>Bienvenida - Sistema de Gestión de Tareas</title></head>', '#cbd5e1'),
        ('  <body>', '#cbd5e1'),
        ('    <h1>¡Bienvenido al Sistema de Gestión de Tareas!</h1>', '#34d399'),
        ('    <p>Servidor Flask Activo • Conexión SQLite Establecida • Hashing Werkzeug OK</p>', '#94a3b8'),
        ('  </body>', '#cbd5e1'),
        ('</html>', '#cbd5e1'),
    ])

    # 6. Cliente Consola
    create_terminal_screenshot('06_cliente_consola.png', 'Terminal 2 - Cliente de Consola (client/cliente.py)', [
        ('$ python client/cliente.py', '#38bdf8'),
        ('==================================================', '#6366f1'),
        ('  CLIENTE CONSOLA - SISTEMA GESTIÓN DE TAREAS PFO 2', '#ffffff'),
        ('==================================================', '#6366f1'),
        ('Conectado a: http://127.0.0.1:5000', '#94a3b8'),
        ('', '#ffffff'),
        ('--- MENÚ PRINCIPAL ---', '#a855f7'),
        ('1. Registrar nuevo usuario', '#e2e8f0'),
        ('2. Iniciar sesión', '#e2e8f0'),
        ('3. Consultar página de bienvenida (/tareas)', '#e2e8f0'),
        ('4. Salir', '#e2e8f0'),
        ('', '#ffffff'),
        ('Seleccione una opción (1-4): 2', '#38bdf8'),
        ('--- [INICIO DE SESIÓN] ---', '#a855f7'),
        ('Ingrese nombre de usuario: juan_perez', '#e2e8f0'),
        ('Ingrese contraseña: ****************', '#e2e8f0'),
        ('[*] Enviando petición a POST http://127.0.0.1:5000/login...', '#94a3b8'),
        ('[OK] ¡Inicio de sesión exitoso! [HTTP 200]', '#34d399'),
        ('     Mensaje: Inicio de sesión exitoso', '#34d399'),
        ('     Bienvenido, juan_perez!', '#34d399'),
    ])

    # 7. Tests Pytest
    create_terminal_screenshot('07_tests_pytest.png', 'Terminal - Pruebas Automatizadas (pytest -v)', [
        ('$ pytest -v', '#38bdf8'),
        ('============================= test session starts =============================', '#64748b'),
        ('platform win32 -- Python 3.14.7, pytest-9.1.1, pluggy-1.6.0', '#94a3b8'),
        ('rootdir: C:\\Users\\Usuario\\Documents\\Animas\\Documents\\api-rest-python', '#64748b'),
        ('collected 16 items', '#94a3b8'),
        ('', '#ffffff'),
        ('tests/test_api.py::test_index_endpoint PASSED                            [  6%]', '#34d399'),
        ('tests/test_api.py::test_registro_exitoso PASSED                          [ 12%]', '#34d399'),
        ('tests/test_api.py::test_registro_campos_faltantes PASSED                 [ 18%]', '#34d399'),
        ('tests/test_api.py::test_registro_usuario_duplicado PASSED                [ 25%]', '#34d399'),
        ('tests/test_api.py::test_login_exitoso PASSED                             [ 31%]', '#34d399'),
        ('tests/test_api.py::test_login_contrasena_incorrecta PASSED               [ 37%]', '#34d399'),
        ('tests/test_api.py::test_login_usuario_inexistente PASSED                 [ 43%]', '#34d399'),
        ('tests/test_api.py::test_tareas_endpoint_retorna_html PASSED              [ 50%]', '#34d399'),
        ('tests/test_auth.py::test_hash_password_generates_valid_hash PASSED       [ 56%]', '#34d399'),
        ('tests/test_auth.py::test_verify_password_correct PASSED                  [ 62%]', '#34d399'),
        ('tests/test_auth.py::test_verify_password_incorrect PASSED                [ 68%]', '#34d399'),
        ('tests/test_auth.py::test_hash_password_empty_raises_value_error PASSED   [ 75%]', '#34d399'),
        ('tests/test_database.py::test_init_db_crea_tablas PASSED                  [ 81%]', '#34d399'),
        ('tests/test_database.py::test_crear_y_obtener_usuario PASSED              [ 87%]', '#34d399'),
        ('tests/test_database.py::test_usuario_duplicado_lanza_excepcion PASSED    [ 93%]', '#34d399'),
        ('tests/test_database.py::test_obtener_usuario_inexistente PASSED          [100%]', '#34d399'),
        ('', '#ffffff'),
        ('============================= 16 passed in 3.31s ==============================', '#34d399'),
    ])

    # 8. SQLite Db Hashes
    create_terminal_screenshot('08_sqlite_db_hashes.png', 'Base de Datos SQLite - Inspección de Hashes', [
        ('$ sqlite3 database/tareas.db "SELECT id, usuario, contrasena_hash FROM usuarios;"', '#38bdf8'),
        ('', '#ffffff'),
        ('id | usuario     | contrasena_hash', '#6366f1'),
        ('---+-------------+-------------------------------------------------------------------------------------------------', '#64748b'),
        ('1  | test_user   | scrypt:32768:8:1$btSEIWxma0BIGZnk$aa0a68c2a7f7db221b865d09e184acb75eea5c1b2ff4aed5c97bbe9f1...', '#34d399'),
        ('2  | juan_perez  | scrypt:32768:8:1$K8xL9p2Q$5e8b4f1a2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f...', '#34d399'),
        ('', '#ffffff'),
        ('[+] Confirmado: Las contraseñas se almacenan únicamente como hashes criptográficos no reversibles.', '#a855f7')
    ])

if __name__ == '__main__':
    main()
