# Mi Aplicación de Gestión de Productos y Categorías

Esta es una aplicación de ejemplo que te permite gestionar productos y categorías. Puedes crear, ver, editar y eliminar productos y categorías utilizando una interfaz web.

## En el caso de no tener instalado Django:
pip install django


## Ejecutar el Proyecto:

Crea y aplique las migraciones de ser necesario: ""python manage.py makemigrations"" &  ""python manage.py migrate.""

Ejecuta el servidor: "" python manage.py runserver. ""


## Funciones Principales

- Crear, ver, editar y eliminar categorías.
- Crear, ver, editar y eliminar productos asociados a categorías.
- Iniciar sesión y registrar una cuenta de usuario.
- Búsqueda de productos por nombre.
- Interfaz de usuario amigable.

## Rutas

- **Página Principal:** La página principal muestra una bienvenida y enlaces a otras secciones.
  - Ruta: /
  
- **Lista de Categorías:** Muestra una lista de todas las categorías disponibles.
  - Ruta: /categorias/
  
- **Lista de Productos:** Muestra una lista de todos los productos disponibles.
  - Ruta: /productos/
  
- **Crear Categoría:** Permite crear una nueva categoría.
  - Ruta: /categoria/nueva/
  
- **Crear Producto:** Permite crear un nuevo producto y asociarlo a una categoría existente.
  - Ruta: /producto/nuevo/
  
- **Buscar Productos:** Permite buscar productos por nombre.
  - Ruta: /buscar/
  
- **Iniciar Sesión:** Página de inicio de sesión.
  - Ruta: /login/
  
- **Cerrar Sesión:** Permite cerrar la sesión de usuario.
  - Ruta: /logout/
  
- **Registro:** Permite registrarse como nuevo usuario.
  - Ruta: /register/
  
## Instalación

Sigue estos pasos para instalar y ejecutar la aplicación en tu computadora local:

1. Clona este repositorio en tu computadora:

   ```bash
   git clone https://github.com/tuusuario/mi-app-gestion-productos.git

## Ve al directorio de la aplicación: 
 cd mi-app-gestion-productos

## Crea un entorno virtual (opcional pero recomendado):
  python -m venv venv

## Activa el entorno virtual:

En Windows: venv\Scripts\activate  En macOS y Linux: source venv/bin/activate

## Instala las dependencias:
  pip install -r requirements.txt

## Realiza las migraciones de la base de datos:
  python manage.py migrate

## Crea un superusuario (administrador) para acceder al panel de administración de Django:
  python manage.py createsuperuser

## Inicia el servidor de desarrollo:
  python manage.py runserver

Abre tu navegador web y visita http://localhost:8000 para acceder a la aplicación.

Para acceder al panel de administración, visita http://localhost:8000/admin y utiliza las credenciales del superusuario que creaste en el paso 7.

¡Listo! Ahora puedes comenzar a utilizar la aplicación y explorar todas sus funciones.





