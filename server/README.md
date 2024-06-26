# Server
Aquí se encuentra la documentación del **servidor de la aplicación FAF**. Se trata 
de una API hecha en Python con Django y `django-rest-framework`, que utiliza MySQL
como base de datos.

## Instalación

Prerrequisitos:

- Tener instalado Python versión 3 y `pip`
- Tener instalado virtualenv
  - Si no lo tienes instalado, se instala simplemente con `pip install virtualenv`, y ya queda 
  habilitado globalmente
- Tener un servidor mysql corriendo
  - Para instalarlo en Windows, se puede descargar el instalador desde [la página oficial](https://dev.mysql.com/downloads/installer/)

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