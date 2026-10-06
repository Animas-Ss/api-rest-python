from werkzeug.security import generate_password_hash, check_password_hash

def hash_password(password: str) -> str:
    """
    Genera un hash seguro para la contraseña proporcionada utilizando pbkdf2:sha256 por defecto.
    Nunca se debe almacenar la contraseña en texto plano.
    """
    if not password or not isinstance(password, str):
        raise ValueError("La contraseña debe ser una cadena de texto no vacía.")
    return generate_password_hash(password)

def verify_password(stored_hash: str, password: str) -> bool:
    """
    Verifica si la contraseña ingresada coincide con el hash almacenado.
    """
    if not stored_hash or not password:
        return False
    return check_password_hash(stored_hash, password)
