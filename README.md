# ¡Bienvenido a Yunou!
Yunou, es una aplicación de tipo cuestionario, desarrollada en 2021. 
Las preguntas están totalmente relacionadas a sucesos en la provincia del Chaco; podrían ser parte de las siguientes categorías: geografía, historia, deportes, arte, cultura, etc.

## Instalaciones
**Instalar Python**

- Comprueba si lo tienes descargado: 
`> python --version`
- Instala o actualiza python; podrás descargarlo de su página oficial https://www.python.org/downloads/

**Instalar el manejador de paquetes "pip"**
- Comprueba si lo tienes descargado con el comando:
`> pip`
- Descarga el script de instalación get-pip-py desde el siguiente enlace:  https://bootstrap.pypa.io/get-pip.py, guardalo con: ` Ctrl + G`
- Abre tu consola de comandos, posicionate sobre el directorio donde guardaste el archivo y ejecuta el siguiente comando: `python get-pip.py`

**Instalar un entorno virtual**
1. Deberás tener una carpeta destinada para el proyecto, por ejemplo, `C:\Users\Desktop\Proyecto>`
2. Posicionado en ella, dentro de la consola instala: 
`> pip install virtualenv`
3. Crea el entorno virtual con el comando:
`> python -m venv <designa un nombre a la carpeta de entorno>`
4. Activa el entorno:
   `C:\Users\Desktop\Proyecto>  <nombre_entorno>\Scripts\activate`
5. Debería de quedar así:
` (nombre_entorno) C:\Users\Desktop\Proyecto>`

**Clonar el repositorio**
- En tu carpeta Proyecto dentro de la consola, escribe:
 ` git clone https://github.com/Syferk/trabajofinal.git`

**Instalar los requerimientos**
- Accede a trabajofinal e instala requeriments.txt:
`C:\Users\Desktop\Proyecto\trabajofinal> python -m pip install -r requirements.txt`

**Ejecuciones**
------------
- Accede a la carpeta proyectofinal:
`C:\Users\Desktop\Proyecto\trabajofinal> cd proyectofinal`

**Migraciones**
- Ejecuta los siguientes comandos:
`python manage.py makemigrations`;
`python manage.py migrate`;
`python manage.py cargar_datos`;

**Creación de admin y ejecución de servidor**
- Ejecuta los siguientes comandos:
`python manage.py createsuperuser`;
`python manage.py runserver`;


# ¡Disfruta de Yunou!

> Regístrate e inicia sesión.

![](https://github.com/Syferk/trabajofinal/blob/desarrollo_iara/proyectofinal/static/images/registrar.png)

> Elige la categoría en la que quieres jugar.

![](https://github.com/Syferk/trabajofinal/blob/desarrollo_iara/proyectofinal/static/images/jugar3.png)

> Visualiza tus resultados y estadísticas

![](https://github.com/Syferk/trabajofinal/blob/desarrollo_iara/proyectofinal/static/images/jugar4.png)
