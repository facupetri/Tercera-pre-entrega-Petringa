# Pre-entrega 3 Petringa

## Descripción

Este proyecto es una página web que gestiona tres modelos de datos. Los usuarios pueden guardar y buscar datos a través de formularios asociados a cada modelo. El proyecto está construido con Django, un framework de desarrollo web en Python.

## Instalación

Para instalar y ejecutar este proyecto, sigue estos pasos:

1. **Clona el Repositorio**

   ```bash
   git clone https://github.com/usuario/pre-entrega-3-petringa.git
   cd pre-entrega-3-petringa
   
# Configura el Entorno Virtual
# Asegúrate de tener Python instalado y crea un entorno virtual:

python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate

# Instala las Dependencias

pip install -r requirements.txt
Configura la Base de Datos

# La configuración por defecto debería estar en settings.py. Asegúrate de que esté correctamente configurada para tu entorno.

# Aplica Migraciones

python manage.py migrate

# Carga Datos Iniciales

# Si tienes datos iniciales para cargar, asegúrate de seguir las instrucciones específicas que puedan estar en el proyecto.

## Estructura del Proyecto
# La estructura del proyecto es la siguiente:

PE3/ - Carpeta principal del proyecto.
app/ - Aplicación del proyecto.
__pycache__/ - Directorio de caché de Python.
migrations/ - Migraciones de la base de datos.
static/ - Archivos estáticos del proyecto.
templates/ - Plantillas HTML para la aplicación.
__init__.py - Archivo de inicialización del paquete.
admin.py - Configuración del panel de administración.
apps.py - Configuración de la aplicación.
models.py - Define los modelos de datos para la aplicación.
tests.py - Pruebas de la aplicación.
urls.py - Configuración de URLs para la aplicación.
views.py - Contiene las vistas que gestionan las solicitudes y responden con los datos.
pe3/ - Carpeta original del proyecto.
__pycache__/ - Directorio de caché de Python.
__init__.py - Archivo de inicialización del paquete.
asgi.py - Configuración de ASGI para la aplicación.
settings.py - Configuración del proyecto.
urls.py - Configuración de URLs para el proyecto.
views.py - Contiene las vistas globales del proyecto.
wsgi.py - Configuración de WSGI para la aplicación.
venv1/ - Entorno virtual del proyecto.
db.sqlite3 - Base de datos SQLite.
manage.py - Herramienta de línea de comandos para gestionar el proyecto Django.

# Funcionalidades
# Carga de Datos

Descripción: Permite a los usuarios guardar datos en la base de datos a través de formularios.
Cómo Probar: Navega a las páginas correspondientes para cada modelo y utiliza los formularios para ingresar datos.
Búsqueda de Datos

# Para iniciar el servidor de desarrollo y ver la aplicación en tu navegador, usa el siguiente comando:

python manage.py runserver
Luego, abre tu navegador y dirígete a http://127.0.0.1:8000/ para ver la aplicación en acción.
