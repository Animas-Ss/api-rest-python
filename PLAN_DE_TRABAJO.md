# PFO 2 — Plan de Trabajo

## Sistema de Gestión de Tareas con API y Base de Datos

---

## Objetivo

Desarrollar un sistema compuesto por una API REST utilizando Flask, una base de datos SQLite y un cliente de consola que permita interactuar con la API.

El proyecto deberá implementar registro de usuarios, inicio de sesión, protección de contraseñas mediante hashing y acceso al endpoint de tareas.

---

# Etapa 1 — Análisis y estructura del proyecto

- [x] Analizar la consigna del PFO 2.
- [x] Definir la arquitectura general del proyecto.
- [x] Crear la carpeta principal del proyecto.
- [x] Crear la carpeta `server/`.
- [x] Crear la carpeta `client/`.
- [x] Crear la carpeta `database/`.
- [x] Crear la carpeta `tests/`.
- [x] Crear la carpeta `screenshots/`.
- [x] Crear `server/__init__.py`.
- [x] Crear `server/servidor.py`.
- [x] Crear `server/database.py`.
- [x] Crear `server/auth.py`.
- [x] Crear `client/cliente.py`.
- [x] Crear `tests/__init__.py`.
- [x] Crear `tests/test_database.py`.
- [x] Crear `tests/test_api.py`.
- [x] Crear `requirements.txt`.
- [x] Crear `.gitignore`.
- [x] Crear `README.md`.
- [x] Crear `PLAN_DE_TRABAJO.md`.

---

# Etapa 2 — Configuración del entorno

- [x] Verificar la versión de Python.
- [x] Crear entorno virtual.
- [x] Activar el entorno virtual.
- [x] Instalar Flask.
- [x] Instalar librería para hashing de contraseñas.
- [x] Instalar pytest.
- [x] Registrar las dependencias en `requirements.txt`.
- [x] Verificar que las dependencias se instalen correctamente.
- [x] Configurar `.gitignore`.
- [x] Verificar que archivos innecesarios no sean incluidos en Git.

---

# Etapa 3 — Configuración inicial de Flask

- [x] Crear la aplicación Flask.
- [x] Configurar `servidor.py` como punto de entrada.
- [x] Crear una ruta inicial de prueba.
- [x] Ejecutar el servidor Flask.
- [x] Verificar que el servidor inicie correctamente.
- [x] Verificar una respuesta HTTP desde el navegador.
- [x] Verificar una respuesta HTTP desde una herramienta de pruebas.

---

# Etapa 4 — Implementación de SQLite

La persistencia del proyecto deberá realizarse mediante SQLite.

## Base de datos

- [x] Crear `database.py`.
- [x] Definir la ubicación de la base de datos.
- [x] Crear función de conexión.
- [x] Crear función para inicializar las tablas.
- [x] Crear tabla `usuarios`.
- [x] Definir `id` de usuario.
- [x] Definir campo `usuario`.
- [x] Definir campo para almacenar la contraseña hasheada.
- [x] Crear tabla `tareas` según las necesidades de la implementación.
- [x] Comprobar la creación de las tablas.
- [x] Comprobar inserción de datos.
- [x] Comprobar consulta de datos.
- [x] Implementar manejo básico de errores de SQLite.

---

# Etapa 5 — Hashing y protección de contraseñas

La consigna establece que las contraseñas no deben almacenarse en texto plano.

- [x] Elegir la librería de hashing.
- [x] Configurar la librería.
- [x] Crear función para generar el hash.
- [x] Crear función para verificar una contraseña.
- [x] Comprobar que una contraseña genere un hash.
- [x] Comprobar que la contraseña original no se almacene en SQLite.
- [x] Comprobar una contraseña correcta.
- [x] Comprobar el rechazo de una contraseña incorrecta.

---

# Etapa 6 — Registro de usuarios

Implementar:

```text
POST /registro
```

El endpoint deberá recibir datos en formato JSON:

```json
{
    "usuario": "nombre",
    "contraseña": "1234"
}
```

Tareas:

- [x] Crear endpoint `/registro`.
- [x] Recibir información mediante JSON.
- [x] Validar que exista el usuario.
- [x] Validar que exista la contraseña.
- [x] Validar los datos recibidos.
- [x] Verificar si el usuario ya existe.
- [x] Generar el hash de la contraseña.
- [x] Guardar el usuario en SQLite.
- [x] No almacenar la contraseña en texto plano.
- [x] Crear respuesta para registro exitoso.
- [x] Crear respuesta para datos inválidos.
- [x] Crear respuesta para usuario duplicado.
- [x] Probar el endpoint manualmente.
- [x] Probar el endpoint mediante tests.

---

# Etapa 7 — Inicio de sesión

Implementar:

```text
POST /login
```

El endpoint deberá verificar las credenciales del usuario.

Tareas:

- [x] Crear endpoint `/login`.
- [x] Recibir usuario y contraseña mediante JSON.
- [x] Buscar el usuario en SQLite.
- [x] Verificar la contraseña contra el hash almacenado.
- [x] Permitir el acceso cuando las credenciales sean correctas.
- [x] Rechazar usuario inexistente.
- [x] Rechazar contraseña incorrecta.
- [x] Crear respuestas HTTP apropiadas.
- [x] Probar login exitoso.
- [x] Probar login incorrecto.
- [x] Probar usuario inexistente.
- [x] Crear tests automatizados.

---

# Etapa 8 — Gestión / acceso a tareas

Implementar:

```text
GET /tareas
```

La consigna establece que este endpoint debe mostrar un HTML de bienvenida.

Tareas:

- [x] Crear endpoint `/tareas`.
- [x] Crear HTML de bienvenida.
- [x] Verificar respuesta desde navegador.
- [x] Verificar código de respuesta HTTP.
- [x] Determinar el comportamiento del endpoint respecto al inicio de sesión.
- [x] Probar acceso correcto.
- [x] Probar acceso no autorizado, si corresponde a la implementación final.
- [x] Crear tests automatizados.

---

# Etapa 9 — Cliente de consola

Desarrollar un cliente que interactúe con la API.

## Funcionalidades

- [x] Crear `client/cliente.py`.
- [x] Implementar conexión con la API.
- [x] Crear menú principal.
- [x] Implementar opción de registro.
- [x] Implementar envío de datos a `/registro`.
- [x] Mostrar respuesta del servidor.
- [x] Implementar opción de login.
- [x] Enviar credenciales a `/login`.
- [x] Mostrar resultado del login.
- [x] Implementar acceso a `/tareas`.
- [x] Mostrar respuesta recibida.
- [x] Manejar errores de conexión.
- [x] Manejar errores HTTP.
- [x] Probar flujo completo desde consola.

---

# Etapa 10 — Manejo de errores

Implementar manejo de errores previsibles.

## API

- [x] Manejar JSON inválido.
- [x] Manejar campos faltantes.
- [x] Manejar usuario duplicado.
- [x] Manejar usuario inexistente.
- [x] Manejar contraseña incorrecta.
- [x] Manejar errores de SQLite.
- [x] Utilizar códigos de estado HTTP adecuados.
- [x] Evitar que errores controlados detengan el servidor.

## Cliente

- [x] Manejar servidor no disponible.
- [x] Manejar errores de conexión.
- [x] Manejar respuestas HTTP con error.
- [x] Mostrar mensajes comprensibles al usuario.

---

# Etapa 11 — Tests automatizados

## Tests de base de datos

- [x] Probar creación de tablas.
- [x] Probar conexión SQLite.
- [x] Probar registro de usuario.
- [x] Probar consulta de usuario.
- [x] Probar errores de base de datos.

## Tests de autenticación

- [x] Probar generación de hash.
- [x] Probar contraseña correcta.
- [x] Probar contraseña incorrecta.

## Tests de API

- [x] Probar `POST /registro`.
- [x] Probar registro exitoso.
- [x] Probar registro inválido.
- [x] Probar usuario duplicado.
- [x] Probar `POST /login`.
- [x] Probar login exitoso.
- [x] Probar login incorrecto.
- [x] Probar usuario inexistente.
- [x] Probar `GET /tareas`.

## Test final

- [x] Ejecutar todos los tests.
- [x] Verificar que todos finalicen correctamente.
- [x] Registrar el resultado final de pytest.

Comando esperado:

```bash
pytest -v
```

---

# Etapa 12 — Pruebas manuales

- [x] Iniciar el servidor.
- [x] Probar registro.
- [x] Comprobar usuario en SQLite.
- [x] Comprobar que la contraseña esté hasheada.
- [x] Probar login correcto.
- [x] Probar login incorrecto.
- [x] Probar usuario inexistente.
- [x] Acceder a `/tareas`.
- [x] Probar el cliente de consola.
- [x] Probar errores previsibles.
- [x] Realizar una prueba completa del sistema.

---

# Etapa 13 — Capturas de pantalla

Crear capturas para documentar el funcionamiento.

- [x] Captura del servidor Flask funcionando.
- [x] Captura del registro exitoso.
- [x] Captura del login exitoso.
- [x] Captura del login incorrecto.
- [x] Captura de `/tareas`.
- [x] Captura del cliente de consola.
- [x] Captura de los tests exitosos.
- [x] Organizar capturas en `screenshots/`.
- [x] Seleccionar las capturas necesarias para la entrega.

---

# Etapa 14 — README.md

Crear la documentación del proyecto.

- [x] Descripción del proyecto.
- [x] Objetivo.
- [x] Tecnologías utilizadas.
- [x] Requisitos.
- [x] Estructura del proyecto.
- [x] Instalación.
- [x] Configuración del entorno.
- [x] Instalación de dependencias.
- [x] Ejecución del servidor.
- [x] Ejecución del cliente.
- [x] Documentación de endpoints.
- [x] Ejemplos de requests.
- [x] Ejemplos de respuestas.
- [x] Ejecución de tests.
- [x] Información sobre SQLite.
- [x] Información sobre hashing.
- [x] Capturas de funcionamiento.
- [x] Instrucciones para reproducir el proyecto.

---

# Etapa 15 — Respuestas conceptuales

Responder las preguntas solicitadas en la consigna.

## 1. ¿Por qué hashear contraseñas?

- [x] Elaborar respuesta.
- [x] Explicar diferencia entre contraseña y hash.
- [x] Explicar el riesgo de almacenar contraseñas en texto plano.
- [x] Relacionar la explicación con la implementación realizada.

## 2. Ventajas de utilizar SQLite

- [x] Elaborar respuesta.
- [x] Explicar por qué SQLite resulta adecuado para este proyecto.
- [x] Relacionar la explicación con la implementación realizada.

---

# Etapa 16 — Revisión final

- [x] Revisar estructura del proyecto.
- [x] Revisar código.
- [x] Revisar endpoints.
- [x] Revisar base de datos.
- [x] Revisar hashing.
- [x] Revisar cliente.
- [x] Ejecutar todos los tests.
- [x] Realizar pruebas manuales.
- [x] Revisar README.
- [x] Revisar capturas.
- [x] Revisar respuestas conceptuales.
- [x] Revisar `.gitignore`.
- [x] Verificar que no haya contraseñas reales ni información sensible.
- [x] Verificar que el proyecto pueda ejecutarse desde cero.

---

# Etapa 17 — Git y GitHub

- [x] Revisar `git status`.
- [x] Revisar archivos que serán incluidos.
- [x] Crear commit del proyecto.
- [x] Subir cambios a GitHub.
- [x] Verificar repositorio remoto.
- [x] Verificar estructura del repositorio.
- [x] Verificar README en GitHub.
- [x] Configurar GitHub Pages según los requisitos de la entrega.
- [x] Verificar que GitHub Pages funcione correctamente.
- [x] Obtener enlace final del repositorio.
- [x] Obtener enlace final de GitHub Pages.

---

# Estado del proyecto

| Etapa | Estado |
|---|---|
| 1. Análisis y estructura | ✅ Completado |
| 2. Configuración del entorno | ✅ Completado |
| 3. Flask | ✅ Completado |
| 4. SQLite | ✅ Completado |
| 5. Hashing | ✅ Completado |
| 6. Registro | ✅ Completado |
| 7. Login | ✅ Completado |
| 8. Tareas | ✅ Completado |
| 9. Cliente | ✅ Completado |
| 10. Manejo de errores | ✅ Completado |
| 11. Tests | ✅ Completado |
| 12. Pruebas manuales | ✅ Completado |
| 13. Capturas | ✅ Completado |
| 14. README | ✅ Completado |
| 15. Respuestas conceptuales | ✅ Completado |
| 16. Revisión final | ✅ Completado |
| 17. GitHub / Entrega | ✅ Completado |