# Mini-Spotify---API-RESTful
Esta una API RESTful que simula una parte del backend de Spotify, enfocada en la gestión de canciones. Esta API permitirá listar canciones, clasificarlas por duración y dar de baja canciones sin borrarlas físicamente.

## Tecnologías utilizadas
* Python 3
* MySQL
* MySQL Workbench
* Flask
* SQLAlchemy

## Endpoints

* GET /api/spotify/canciones
Devuelve todas las canciones activas del catálogo.

* DELETE /api/spotify/canciones/<int:id>
Realiza una baja lógica: cambia el estado de la canción a "inactiva".

* GET /api/spotify/canciones/clasificadas
Retorna las canciones activas agrupadas por duración:
    Corta: menos de 180 segundos 
    Media: entre 180 y 240 segundos
    Larga: más de 340 segundos

## Correr proyecto

1. Clonar el proyecto:

`git clone https://github.com/tu-usuario/tu-repo.git`

2. Crear entorno virtual:

· Windows:

`python -m venv <environment_name>`

· Linux/macOS:

`python3 -m venv <environment_name>`

3. Activar entorno virtual:

· Windows:

`<environment_name>\Scripts\activate`

· Linux / macOS:

`source <environment_name>/bin/activate`

4. Instalar dependencias:

· Windows, Linux, y macOS:

`pip install -r requirements.txt`

5. Correr aplicación:

`python app.py` 