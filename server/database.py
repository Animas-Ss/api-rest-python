import os
import sqlite3

# Ruta por defecto de la base de datos dentro de la carpeta 'database'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_DIR = os.path.join(BASE_DIR, 'database')
DEFAULT_DB_PATH = os.path.join(DB_DIR, 'tareas.db')

def get_db_connection(db_path=None):
    """
    Establece y retorna una conexión a la base de datos SQLite.
    Si la carpeta de la base de datos no existe, se crea automáticamente.
    """
    if db_path is None:
        db_path = DEFAULT_DB_PATH

    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def init_db(db_path=None):
    """
    Inicializa las tablas necesarias en la base de datos SQLite.
    """
    conn = get_db_connection(db_path)
    cursor = conn.cursor()

    # Tabla de usuarios
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT UNIQUE NOT NULL,
            contrasena_hash TEXT NOT NULL,
            creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Tabla de tareas (opcional/escalable)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tareas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER NOT NULL,
            titulo TEXT NOT NULL,
            descripcion TEXT,
            completada BOOLEAN DEFAULT 0,
            creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (usuario_id) REFERENCES usuarios (id) ON DELETE CASCADE
        )
    ''')

    conn.commit()
    conn.close()

def crear_usuario(usuario, contrasena_hash, db_path=None):
    """
    Inserta un nuevo usuario en la base de datos.
    Retorna el ID del usuario registrado.
    Lanza sqlite3.IntegrityError si el usuario ya existe.
    """
    conn = get_db_connection(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO usuarios (usuario, contrasena_hash) VALUES (?, ?)",
            (usuario, contrasena_hash)
        )
        conn.commit()
        usuario_id = cursor.lastrowid
        return usuario_id
    finally:
        conn.close()

def obtener_usuario_por_nombre(usuario, db_path=None):
    """
    Obtiene un usuario de la base de datos por su nombre de usuario.
    Retorna sqlite3.Row con los datos del usuario o None si no existe.
    """
    conn = get_db_connection(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute(
            "SELECT * FROM usuarios WHERE usuario = ?",
            (usuario,)
        )
        user = cursor.fetchone()
        return user
    finally:
        conn.close()
