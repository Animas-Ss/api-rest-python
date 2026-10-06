import os
import sqlite3
from flask import Flask, request, jsonify, render_template_string
from server.database import init_db, crear_usuario, obtener_usuario_por_nombre
from server.auth import hash_password, verify_password

def create_app(db_path=None):
    app = Flask(__name__)
    app.config['DB_PATH'] = db_path

    # Asegurar que la base de datos esté inicializada al arrancar la app
    with app.app_context():
        init_db(app.config['DB_PATH'])

    @app.errorhandler(400)
    def bad_request_error(e):
        return jsonify({"error": "Solicitud incorrecta o JSON inválido"}), 400

    @app.errorhandler(404)
    def not_found_error(e):
        return jsonify({"error": "Recurso no encontrado"}), 404

    @app.errorhandler(500)
    def internal_error(e):
        return jsonify({"error": "Error interno del servidor"}), 500

    @app.route('/', methods=['GET'])
    def index():
        return jsonify({
            "nombre": "API REST - Sistema de Gestión de Tareas (PFO 2)",
            "version": "1.0.0",
            "endpoints": {
                "POST /registro": "Registra un nuevo usuario con contraseña hasheada",
                "POST /login": "Inicia sesión verificando credenciales",
                "GET /tareas": "Muestra la página de bienvenida a la gestión de tareas"
            }
        }), 200

    @app.route('/registro', methods=['POST'])
    def registro():
        """
        Endpoint de registro de usuarios.
        Espera JSON: {"usuario": "nombre", "contraseña": "1234"}
        Soporta también la clave 'contrasena' por compatibilidad.
        """
        data = request.get_json(silent=True)
        if not data or not isinstance(data, dict):
            return jsonify({"error": "Se requiere un cuerpo en formato JSON válido"}), 400

        usuario = data.get('usuario')
        # Soporta 'contraseña' (según consigna) y 'contrasena'
        contrasena = data.get('contraseña') if 'contraseña' in data else data.get('contrasena')

        if not usuario or not contrasena:
            return jsonify({"error": "Faltan campos requeridos: 'usuario' y 'contraseña'"}), 400

        usuario = str(usuario).strip()
        contrasena = str(contrasena).strip()

        if not usuario or not contrasena:
            return jsonify({"error": "El nombre de usuario y la contraseña no pueden estar vacíos"}), 400

        # Verificar si el usuario ya existe
        db_path = app.config.get('DB_PATH')
        usuario_existente = obtener_usuario_por_nombre(usuario, db_path=db_path)
        if usuario_existente:
            return jsonify({"error": "El usuario ya existe"}), 409

        # Hashear la contraseña
        password_hash = hash_password(contrasena)

        try:
            crear_usuario(usuario, password_hash, db_path=db_path)
            return jsonify({
                "mensaje": "Usuario registrado exitosamente",
                "usuario": usuario
            }), 201
        except sqlite3.IntegrityError:
            return jsonify({"error": "El usuario ya existe"}), 409
        except Exception as e:
            return jsonify({"error": f"Error al registrar usuario: {str(e)}"}), 500

    @app.route('/login', methods=['POST'])
    def login():
        """
        Endpoint de inicio de sesión.
        Espera JSON: {"usuario": "nombre", "contraseña": "1234"}
        Soporta también la clave 'contrasena' por compatibilidad.
        """
        data = request.get_json(silent=True)
        if not data or not isinstance(data, dict):
            return jsonify({"error": "Se requiere un cuerpo en formato JSON válido"}), 400

        usuario = data.get('usuario')
        contrasena = data.get('contraseña') if 'contraseña' in data else data.get('contrasena')

        if not usuario or not contrasena:
            return jsonify({"error": "Faltan campos requeridos: 'usuario' y 'contraseña'"}), 400

        usuario = str(usuario).strip()
        contrasena = str(contrasena).strip()

        db_path = app.config.get('DB_PATH')
        user = obtener_usuario_por_nombre(usuario, db_path=db_path)

        if not user or not verify_password(user['contrasena_hash'], contrasena):
            return jsonify({"error": "Credenciales inválidas"}), 401

        return jsonify({
            "mensaje": "Inicio de sesión exitoso",
            "usuario": user['usuario']
        }), 200

    @app.route('/tareas', methods=['GET'])
    def tareas():
        """
        Endpoint de gestión de tareas.
        Consigna: Muestre un html de bienvenida.
        """
        html_content = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bienvenida - Sistema de Gestión de Tareas</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Outfit', sans-serif;
            background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #0f172a 100%);
            color: #f8fafc;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 2rem;
        }
        .container {
            background: rgba(30, 41, 59, 0.7);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 24px;
            padding: 3rem 2.5rem;
            max-width: 650px;
            width: 100%;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5), 0 0 30px rgba(99, 102, 241, 0.2);
            text-align: center;
            animation: fadeIn 0.8s ease-out;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .badge {
            display: inline-block;
            background: linear-gradient(90deg, #6366f1, #a855f7);
            color: #ffffff;
            font-size: 0.85rem;
            font-weight: 600;
            padding: 0.4rem 1rem;
            border-radius: 50px;
            margin-bottom: 1.5rem;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        h1 {
            font-size: 2.5rem;
            font-weight: 700;
            background: linear-gradient(90deg, #ffffff, #cbd5e1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 1rem;
            line-height: 1.2;
        }
        p.subtitle {
            color: #94a3b8;
            font-size: 1.1rem;
            margin-bottom: 2rem;
            line-height: 1.6;
        }
        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 1.2rem;
            margin-top: 2rem;
            text-align: left;
        }
        .feature-card {
            background: rgba(15, 23, 42, 0.6);
            border: 1px solid rgba(255, 255, 255, 0.05);
            padding: 1.2rem;
            border-radius: 16px;
            transition: transform 0.3s ease, border-color 0.3s ease;
        }
        .feature-card:hover {
            transform: translateY(-4px);
            border-color: rgba(99, 102, 241, 0.4);
        }
        .feature-icon {
            font-size: 1.8rem;
            margin-bottom: 0.5rem;
        }
        .feature-title {
            font-weight: 600;
            color: #e2e8f0;
            margin-bottom: 0.3rem;
        }
        .feature-desc {
            font-size: 0.9rem;
            color: #64748b;
        }
        .status-box {
            margin-top: 2rem;
            padding: 1rem;
            background: rgba(16, 185, 129, 0.1);
            border: 1px solid rgba(16, 185, 129, 0.3);
            border-radius: 12px;
            color: #34d399;
            font-weight: 500;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.5rem;
        }
        .pulse-dot {
            width: 10px;
            height: 10px;
            background-color: #34d399;
            border-radius: 50%;
            box-shadow: 0 0 10px #34d399;
            animation: pulse 2s infinite;
        }
        @keyframes pulse {
            0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(52, 211, 153, 0.7); }
            70% { transform: scale(1); box-shadow: 0 0 0 10px rgba(52, 211, 153, 0); }
            100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(52, 211, 153, 0); }
        }
        footer {
            margin-top: 2.5rem;
            font-size: 0.85rem;
            color: #475569;
        }
    </style>
</head>
<body>
    <div class="container">
        <span class="badge">PFO 2 — API REST Flask</span>
        <h1>¡Bienvenido al Sistema de Gestión de Tareas!</h1>
        <p class="subtitle">Has accedido exitosamente al módulo de tareas. El servidor Flask y la persistencia SQLite se encuentran operando correctamente.</p>
        
        <div class="status-box">
            <div class="pulse-dot"></div>
            <span>Servidor Activo • Conexión SQLite Establecida • Hashing Werkzeug OK</span>
        </div>

        <div class="features-grid">
            <div class="feature-card">
                <div class="feature-icon">🔒</div>
                <div class="feature-title">Seguridad Hashing</div>
                <div class="feature-desc">Contraseñas protegidas mediante algoritmos de hash seguro.</div>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🗄️</div>
                <div class="feature-title">Base de Datos</div>
                <div class="feature-desc">Persistencia de usuarios y datos relacionales con SQLite.</div>
            </div>
            <div class="feature-card">
                <div class="feature-icon">⚡</div>
                <div class="feature-title">API RESTful</div>
                <div class="feature-desc">Endpoints estructurados para registro, login y gestión.</div>
            </div>
            <div class="feature-card">
                <div class="feature-icon">💻</div>
                <div class="feature-title">Cliente Consola</div>
                <div class="feature-desc">Interacción remota fluida desde la terminal interactiva.</div>
            </div>
        </div>

        <footer>
            Trabajo Práctico Obligatorio 2 — Sistema de Gestión de Tareas
        </footer>
    </div>
</body>
</html>"""
        return render_template_string(html_content), 200

    return app

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"[+] Iniciando servidor Flask en http://127.0.0.1:{port}")
    app.run(host='127.0.0.1', port=port, debug=True)
