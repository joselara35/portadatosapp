FROM python:3.11

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Instalar dependencias del sistema requeridas para las bibliotecas de Python
RUN apt-get update && \
    apt-get install -y libpq-dev gcc && \
    apt-get clean

# Copiar el archivo de requisitos para instalar paquetes de Python
COPY requirements.txt ./

# Instalar los paquetes requeridos por la aplicación
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todos los archivos del proyecto Django al contenedor
COPY . .

# Exponer el puerto que usará Gunicorn (o tu servidor de aplicaciones WSGI)
EXPOSE 8000

# Ejecutar el servidor de aplicaciones Gunicorn para servir la aplicación Django
CMD ["gunicorn", "portadatos_python.wsgi:application", "--bind", "0.0.0.0:8000"]
