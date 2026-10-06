import pytest
from server.auth import hash_password, verify_password

def test_hash_password_generates_valid_hash():
    password = "mi_contraseña_secreta_123"
    hashed = hash_password(password)
    
    assert hashed != password
    assert isinstance(hashed, str)
    assert len(hashed) > 10

def test_verify_password_correct():
    password = "password123"
    hashed = hash_password(password)
    
    assert verify_password(hashed, password) is True

def test_verify_password_incorrect():
    password = "password123"
    hashed = hash_password(password)
    
    assert verify_password(hashed, "password_errada") is False

def test_hash_password_empty_raises_value_error():
    with pytest.raises(ValueError):
        hash_password("")
