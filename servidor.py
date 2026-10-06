"""
Punto de entrada principal para ejecutar el servidor Flask del PFO 2.
"""
from server.servidor import app

if __name__ == '__main__':
    print("[+] Iniciando servidor Flask (Sistema de Gestion de Tareas)...")
    app.run(host='127.0.0.1', port=5000, debug=True)
