Instalación

Prerrequisitos:

- Tener instalado Python 3
- Tener instalado virtualenv (`pip install virtualenv`)
- Tener un servidor mysql corriendo

Pasos

1. Ir al directorio del server: `cd server`
2. Crear un archivo `.env`, completando las variables presentes en el `.env.example` con los
   datos de conexión a la base:
   ```env
   DB_NAME=
   DB_USER=
   DB_PASSWORD=
   DB_HOST=
   DB_PORT=
   ```
1. Crear un entorno virtual de python: `virtualenv venv`
2. Activar el entorno virtual:
    3. Linux: `source venv/bin/activate`
    4. Windows: `.\venv\bin\activate`
5. Instalar las librerías requeridas: `pip install -r requirements.txt`
6. Ejecutar las migraciones de configuración: `python manage.py migrate`
7. Crear un usuario superuser: `python manage.py createsuperuser`
8. Para correr el servidor, ejecutar: `python manage.py runserver`
9. Acceder a la dirección `http://localhost:8000/admin` para ver la aplicación