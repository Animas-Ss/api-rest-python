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
- [ ] Verificar que archivos innecesarios no sean incluidos en Git.

---

# Etapa 3 — Configuración inicial de Flask

- [ ] Crear la aplicación Flask.
- [ ] Configurar `servidor.py` como punto de entrada.
- [ ] Crear una ruta inicial de prueba.
- [ ] Ejecutar el servidor Flask.
- [ ] Verificar que el servidor inicie correctamente.
- [ ] Verificar una respuesta HTTP desde el navegador.
- [ ] Verificar una respuesta HTTP desde una herramienta de pruebas.

---

# Etapa 4 — Implementación de SQLite

La persistencia del proyecto deberá realizarse mediante SQLite.

## Base de datos

- [ ] Crear `database.py`.
- [ ] Definir la ubicación de la base de datos.
- [ ] Crear función de conexión.
- [ ] Crear función para inicializar las tablas.
- [ ] Crear tabla `usuarios`.
- [ ] Definir `id` de usuario.
- [ ] Definir campo `usuario`.
- [ ] Definir campo para almacenar la contraseña hasheada.
- [ ] Crear tabla `tareas` según las necesidades de la implementación.
- [ ] Comprobar la creación de las tablas.
- [ ] Comprobar inserción de datos.
- [ ] Comprobar consulta de datos.
- [ ] Implementar manejo básico de errores de SQLite.

---

# Etapa 5 — Hashing y protección de contraseñas

La consigna establece que las contraseñas no deben almacenarse en texto plano.

- [ ] Elegir la librería de hashing.
- [ ] Configurar la librería.
- [ ] Crear función para generar el hash.
- [ ] Crear función para verificar una contraseña.
- [ ] Comprobar que una contraseña genere un hash.
- [ ] Comprobar que la contraseña original no se almacene en SQLite.
- [ ] Comprobar una contraseña correcta.
- [ ] Comprobar el rechazo de una contraseña incorrecta.

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

- [ ] Crear endpoint `/registro`.
- [ ] Recibir información mediante JSON.
- [ ] Validar que exista el usuario.
- [ ] Validar que exista la contraseña.
- [ ] Validar los datos recibidos.
- [ ] Verificar si el usuario ya existe.
- [ ] Generar el hash de la contraseña.
- [ ] Guardar el usuario en SQLite.
- [ ] No almacenar la contraseña en texto plano.
- [ ] Crear respuesta para registro exitoso.
- [ ] Crear respuesta para datos inválidos.
- [ ] Crear respuesta para usuario duplicado.
- [ ] Probar el endpoint manualmente.
- [ ] Probar el endpoint mediante tests.

---

# Etapa 7 — Inicio de sesión

Implementar:

```text
POST /login
```

El endpoint deberá verificar las credenciales del usuario.

Tareas:

- [ ] Crear endpoint `/login`.
- [ ] Recibir usuario y contraseña mediante JSON.
- [ ] Buscar el usuario en SQLite.
- [ ] Verificar la contraseña contra el hash almacenado.
- [ ] Permitir el acceso cuando las credenciales sean correctas.
- [ ] Rechazar usuario inexistente.
- [ ] Rechazar contraseña incorrecta.
- [ ] Crear respuestas HTTP apropiadas.
- [ ] Probar login exitoso.
- [ ] Probar login incorrecto.
- [ ] Probar usuario inexistente.
- [ ] Crear tests automatizados.

---

# Etapa 8 — Gestión / acceso a tareas

Implementar:

```text
GET /tareas
```

La consigna establece que este endpoint debe mostrar un HTML de bienvenida.

Tareas:

- [ ] Crear endpoint `/tareas`.
- [ ] Crear HTML de bienvenida.
- [ ] Verificar respuesta desde navegador.
- [ ] Verificar código de respuesta HTTP.
- [ ] Determinar el comportamiento del endpoint respecto al inicio de sesión.
- [ ] Probar acceso correcto.
- [ ] Probar acceso no autorizado, si corresponde a la implementación final.
- [ ] Crear tests automatizados.

> Nota: la consigna no especifica endpoints CRUD para crear, modificar o eliminar tareas. No se agregarán funcionalidades adicionales salvo que sean necesarias para cumplir con los requisitos del trabajo.

---

# Etapa 9 — Cliente de consola

Desarrollar un cliente que interactúe con la API.

## Funcionalidades

- [ ] Crear `client/cliente.py`.
- [ ] Implementar conexión con la API.
- [ ] Crear menú principal.
- [ ] Implementar opción de registro.
- [ ] Implementar envío de datos a `/registro`.
- [ ] Mostrar respuesta del servidor.
- [ ] Implementar opción de login.
- [ ] Enviar credenciales a `/login`.
- [ ] Mostrar resultado del login.
- [ ] Implementar acceso a `/tareas`.
- [ ] Mostrar respuesta recibida.
- [ ] Manejar errores de conexión.
- [ ] Manejar errores HTTP.
- [ ] Probar flujo completo desde consola.

---

# Etapa 10 — Manejo de errores

Implementar manejo de errores previsibles.

## API

- [ ] Manejar JSON inválido.
- [ ] Manejar campos faltantes.
- [ ] Manejar usuario duplicado.
- [ ] Manejar usuario inexistente.
- [ ] Manejar contraseña incorrecta.
- [ ] Manejar errores de SQLite.
- [ ] Utilizar códigos de estado HTTP adecuados.
- [ ] Evitar que errores controlados detengan el servidor.

## Cliente

- [ ] Manejar servidor no disponible.
- [ ] Manejar errores de conexión.
- [ ] Manejar respuestas HTTP con error.
- [ ] Mostrar mensajes comprensibles al usuario.

---

# Etapa 11 — Tests automatizados

## Tests de base de datos

- [ ] Probar creación de tablas.
- [ ] Probar conexión SQLite.
- [ ] Probar registro de usuario.
- [ ] Probar consulta de usuario.
- [ ] Probar errores de base de datos.

## Tests de autenticación

- [ ] Probar generación de hash.
- [ ] Probar contraseña correcta.
- [ ] Probar contraseña incorrecta.

## Tests de API

- [ ] Probar `POST /registro`.
- [ ] Probar registro exitoso.
- [ ] Probar registro inválido.
- [ ] Probar usuario duplicado.
- [ ] Probar `POST /login`.
- [ ] Probar login exitoso.
- [ ] Probar login incorrecto.
- [ ] Probar usuario inexistente.
- [ ] Probar `GET /tareas`.

## Test final

- [ ] Ejecutar todos los tests.
- [ ] Verificar que todos finalicen correctamente.
- [ ] Registrar el resultado final de pytest.

Comando esperado:

```bash
pytest -v
```

---

# Etapa 12 — Pruebas manuales

- [ ] Iniciar el servidor.
- [ ] Probar registro.
- [ ] Comprobar usuario en SQLite.
- [ ] Comprobar que la contraseña esté hasheada.
- [ ] Probar login correcto.
- [ ] Probar login incorrecto.
- [ ] Probar usuario inexistente.
- [ ] Acceder a `/tareas`.
- [ ] Probar el cliente de consola.
- [ ] Probar errores previsibles.
- [ ] Realizar una prueba completa del sistema.

---

# Etapa 13 — Capturas de pantalla

Crear capturas para documentar el funcionamiento.

- [ ] Captura del servidor Flask funcionando.
- [ ] Captura del registro exitoso.
- [ ] Captura del login exitoso.
- [ ] Captura del login incorrecto.
- [ ] Captura de `/tareas`.
- [ ] Captura del cliente de consola.
- [ ] Captura de los tests exitosos.
- [ ] Organizar capturas en `screenshots/`.
- [ ] Seleccionar las capturas necesarias para la entrega.

---

# Etapa 14 — README.md

Crear la documentación del proyecto.

- [ ] Descripción del proyecto.
- [ ] Objetivo.
- [ ] Tecnologías utilizadas.
- [ ] Requisitos.
- [ ] Estructura del proyecto.
- [ ] Instalación.
- [ ] Configuración del entorno.
- [ ] Instalación de dependencias.
- [ ] Ejecución del servidor.
- [ ] Ejecución del cliente.
- [ ] Documentación de endpoints.
- [ ] Ejemplos de requests.
- [ ] Ejemplos de respuestas.
- [ ] Ejecución de tests.
- [ ] Información sobre SQLite.
- [ ] Información sobre hashing.
- [ ] Capturas de funcionamiento.
- [ ] Instrucciones para reproducir el proyecto.

---

# Etapa 15 — Respuestas conceptuales

Responder las preguntas solicitadas en la consigna.

## 1. ¿Por qué hashear contraseñas?

- [ ] Elaborar respuesta.
- [ ] Explicar diferencia entre contraseña y hash.
- [ ] Explicar el riesgo de almacenar contraseñas en texto plano.
- [ ] Relacionar la explicación con la implementación realizada.

## 2. Ventajas de utilizar SQLite

- [ ] Elaborar respuesta.
- [ ] Explicar por qué SQLite resulta adecuado para este proyecto.
- [ ] Relacionar la explicación con la implementación realizada.

---

# Etapa 16 — Revisión final

- [ ] Revisar estructura del proyecto.
- [ ] Revisar código.
- [ ] Revisar endpoints.
- [ ] Revisar base de datos.
- [ ] Revisar hashing.
- [ ] Revisar cliente.
- [ ] Ejecutar todos los tests.
- [ ] Realizar pruebas manuales.
- [ ] Revisar README.
- [ ] Revisar capturas.
- [ ] Revisar respuestas conceptuales.
- [ ] Revisar `.gitignore`.
- [ ] Verificar que no haya contraseñas reales ni información sensible.
- [ ] Verificar que el proyecto pueda ejecutarse desde cero.

---

# Etapa 17 — Git y GitHub

- [ ] Revisar `git status`.
- [ ] Revisar archivos que serán incluidos.
- [ ] Crear commit del proyecto.
- [ ] Subir cambios a GitHub.
- [ ] Verificar repositorio remoto.
- [ ] Verificar estructura del repositorio.
- [ ] Verificar README en GitHub.
- [ ] Configurar GitHub Pages según los requisitos de la entrega.
- [ ] Verificar que GitHub Pages funcione correctamente.
- [ ] Obtener enlace final del repositorio.
- [ ] Obtener enlace final de GitHub Pages.

---

# Estado del proyecto

| Etapa | Estado |
|---|---|
| 1. Análisis y estructura | ⬜ Pendiente |
| 2. Configuración del entorno | ⬜ Pendiente |
| 3. Flask | ⬜ Pendiente |
| 4. SQLite | ⬜ Pendiente |
| 5. Hashing | ⬜ Pendiente |
| 6. Registro | ⬜ Pendiente |
| 7. Login | ⬜ Pendiente |
| 8. Tareas | ⬜ Pendiente |
| 9. Cliente | ⬜ Pendiente |
| 10. Manejo de errores | ⬜ Pendiente |
| 11. Tests | ⬜ Pendiente |
| 12. Pruebas manuales | ⬜ Pendiente |
| 13. Capturas | ⬜ Pendiente |
| 14. README | ⬜ Pendiente |
| 15. Respuestas conceptuales | ⬜ Pendiente |
| 16. Revisión final | ⬜ Pendiente |
| 17. GitHub / Entrega | ⬜ Pendiente |

---

## Criterio de avance

Una tarea se marcará como realizada solamente cuando:

1. Se haya implementado.
2. Se haya probado.
3. Se haya comprobado que funciona.
4. Se encuentre integrada correctamente con el resto del proyecto cuando corresponda.

El objetivo es desarrollar el proyecto de forma incremental, evitando avanzar sobre funcionalidades que todavía no fueron verificadas.