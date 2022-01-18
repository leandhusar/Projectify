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

## API Endpoints
Las siguientes son las rutas de las APIs construidas para este proyecto, con su respectivo método.
**Aclaración: **Solo la API del Token no requiere autenticación, pero es clave para obtener el token JWT para acceder a los otros servicios.

* ### Token /api/token/
**Método**  POST
*Obtiene JWT de un usuario. Estos tokens tienen un ciclo de vida de 5 minutos.*
    ```json
Body = {
    	username: string,
    	password: string
    }
```

* ### Report /api/report/
**Método**  GET
*Obtiene los reportes creados por un usuario.*
    ```json
Authorization = Bearer <user_token>
```
**Método**  POST
*Crea un nuevo reporte. No se crea el reporte si el usuario ya ha creado un reporte de el projecto al que hace referencia durante su semana de creación.*
    ```json
Authorization = Bearer <user_token>
Body = {
    	project: number,
    	percentage: number
    }
```
**Método**  PUT
*Modifica un reporte creado por el usuario. Un usuario no puede modificar un reporte ajeno, ni tampoco reportes hechos en meses pasados.*
    ```javascript
Authorization = Bearer <user_token>
Body = {
    	id: number,
    	percentage: number
    }
```

* ### Project /api/project/
*Obtiene los proyectos de la empresa.*
**Método**  GET
    ```json
Authorization = Bearer <user_token>
```

## Producción
Puede utilizar como URL base del proyecto esta URL: [https://mighty-shore-53449.herokuapp.com](https://mighty-shore-53449.herokuapp.com "https://mighty-shore-53449.herokuapp.com").

Puede acceder a un Token con una cuenta consumiento el servicio */api/token/* con las siguientes credenciales:
* **username:** leanware0
* **password:** Clave123_