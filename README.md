# Projectify

Projectify es una aplicación web que permite a la agencia de publicidad AdsForGood tener visibilidad sobre el estado de sus proyectos de una manera muy simple.

## Instalación
Para instalarlo en su entorno local, descargue este repositorio e inicialice un entorno virtual con Python. Puede crear un entorno virtual siguiendo esta [guía](https://docs.python.org/3/library/venv.html "guía").

Una vez descargado e inicializado el entorno virtual, debe instalar las dependencias de Python para este proyecto, ejecutando el comando:

`pip install -r requirements.txt`

**NOTA:** Debe estar ubicado en la carpeta raíz del proyecto para no tener dificultades.

En caso de tener problemas con la instalación, debe leer el log para encontrar soluciones a sus problemas.

## Inicialización Y Ejecución
Debe iniciar las migraciones en la base de datos, que, por defecto, se crea en una instancia de SQLite, pero su configuración se adapta a variables de entorno. Para esto, ejecute los siguientes comandos:

`python manage.py makemigrations`

`python manage.py migrate`

Luego, debe crear un super-usuario en el sistema, ejecute:

`python manage.py createsuperuser`

Con esto ya podrá ejecutar el proyecto, usando el comando:

`python manage.py runserver`