import sys
import os
import io
import json
import urllib.request
import urllib.error
import argparse

# Configurar encoding seguro para stdout/stderr en entornos Windows con codificación CP1252
if hasattr(sys.stdout, 'buffer'):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'buffer'):
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

DEFAULT_SERVER_URL = "http://127.0.0.1:5000"

def enviar_peticion_post(url, payload):
    """
    Envía una petición POST con payload JSON al servidor.
    Retorna (status_code, response_data_dict_o_str)
    """
    json_bytes = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(
        url,
        data=json_bytes,
        headers={'Content-Type': 'application/json'},
        method='POST'
    )
    try:
        with urllib.request.urlopen(req) as resp:
            status = resp.status
            body = resp.read().decode('utf-8')
            try:
                data = json.loads(body)
            except json.JSONDecodeError:
                data = body
            return status, data
    except urllib.error.HTTPError as e:
        status = e.code
        body = e.read().decode('utf-8')
        try:
            data = json.loads(body)
        except json.JSONDecodeError:
            data = body
        return status, data
    except urllib.error.URLError as e:
        return None, f"Error de conexión con el servidor: {e.reason}"

def enviar_peticion_get(url):
    """
    Envía una petición GET al servidor.
    Retorna (status_code, body_str)
    """
    req = urllib.request.Request(url, method='GET')
    try:
        with urllib.request.urlopen(req) as resp:
            status = resp.status
            body = resp.read().decode('utf-8')
            return status, body
    except urllib.error.HTTPError as e:
        status = e.code
        body = e.read().decode('utf-8')
        return status, body
    except urllib.error.URLError as e:
        return None, f"Error de conexión con el servidor: {e.reason}"

def menu_registro(base_url):
    print("\n--- [REGISTRO DE USUARIO] ---")
    usuario = input("Ingrese nombre de usuario: ").strip()
    if not usuario:
        print("[!] El nombre de usuario no puede estar vacío.")
        return

    contrasena = input("Ingrese contraseña: ").strip()
    if not contrasena:
        print("[!] La contraseña no puede estar vacía.")
        return

    payload = {
        "usuario": usuario,
        "contraseña": contrasena
    }

    url = f"{base_url}/registro"
    print(f"[*] Enviando petición a POST {url}...")
    status, res = enviar_peticion_post(url, payload)

    if status is None:
        print(f"[!] {res}")
    elif status == 201:
        print(f"[OK] ¡Registro exitoso! [HTTP {status}]")
        print(f"     Mensaje: {res.get('mensaje', '')}")
        print(f"     Usuario: {res.get('usuario', '')}")
    else:
        print(f"[!] Error al registrar usuario [HTTP {status}]:")
        if isinstance(res, dict) and 'error' in res:
            print(f"     Detalle: {res['error']}")
        else:
            print(f"     Respuesta: {res}")

def menu_login(base_url):
    print("\n--- [INICIO DE SESIÓN] ---")
    usuario = input("Ingrese nombre de usuario: ").strip()
    contrasena = input("Ingrese contraseña: ").strip()

    if not usuario or not contrasena:
        print("[!] Nombre de usuario y contraseña son requeridos.")
        return

    payload = {
        "usuario": usuario,
        "contraseña": contrasena
    }

    url = f"{base_url}/login"
    print(f"[*] Enviando petición a POST {url}...")
    status, res = enviar_peticion_post(url, payload)

    if status is None:
        print(f"[!] {res}")
    elif status == 200:
        print(f"[OK] ¡Inicio de sesión exitoso! [HTTP {status}]")
        print(f"     Mensaje: {res.get('mensaje', '')}")
        print(f"     Bienvenido, {res.get('usuario', '')}!")
    else:
        print(f"[!] Fallo al iniciar sesión [HTTP {status}]:")
        if isinstance(res, dict) and 'error' in res:
            print(f"     Motivo: {res['error']}")
        else:
            print(f"     Respuesta: {res}")

def menu_tareas(base_url):
    print("\n--- [OBTENER HTML DE BIENVENIDA - /tareas] ---")
    url = f"{base_url}/tareas"
    print(f"[*] Enviando petición a GET {url}...")
    status, body = enviar_peticion_get(url)

    if status is None:
        print(f"[!] {body}")
    elif status == 200:
        print(f"[OK] ¡Respuesta recibida correctamente! [HTTP {status}]")
        print("--- INICIO DE CONTENIDO HTML ---")
        lines = body.splitlines()
        for line in lines[:15]:
            print(line)
        if len(lines) > 15:
            print(f"... ({len(lines) - 15} líneas más)")
        print("--- FIN DE CONTENIDO HTML ---")
    else:
        print(f"[!] Error al consultar /tareas [HTTP {status}]: {body}")

def main():
    parser = argparse.ArgumentParser(description="Cliente Consola API REST PFO 2")
    parser.add_argument("--url", default=DEFAULT_SERVER_URL, help="URL base del servidor Flask")
    args = parser.parse_args()

    base_url = args.url.rstrip('/')

    print("==================================================")
    print("  CLIENTE CONSOLA - SISTEMA GESTIÓN DE TAREAS PFO 2")
    print("==================================================")
    print(f"Conectado a: {base_url}\n")

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar nuevo usuario")
        print("2. Iniciar sesión")
        print("3. Consultar página de bienvenida (/tareas)")
        print("4. Salir")
        
        try:
            opcion = input("\nSeleccione una opción (1-4): ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\nSaliendo del cliente.")
            sys.exit(0)

        if opcion == '1':
            menu_registro(base_url)
        elif opcion == '2':
            menu_login(base_url)
        elif opcion == '3':
            menu_tareas(base_url)
        elif opcion == '4':
            print("\n¡Gracias por utilizar el cliente de consola! Hasta luego.")
            sys.exit(0)
        else:
            print("[!] Opción no válida. Por favor, ingrese un número del 1 al 4.")

if __name__ == '__main__':
    main()
