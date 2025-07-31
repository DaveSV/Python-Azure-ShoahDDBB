# Usa la imagen oficial de Python en su versión slim
ARG PYTHON_VERSION=3.11
FROM python:${PYTHON_VERSION}-slim

# Instala las dependencias del sistema operativo necesarias para compilar librerías de Python.
# Si usas MariaDB/MySQL, necesitas 'default-libmysqlclient-dev'.
# Si usas PostgreSQL, necesitas 'libpq-dev'.
# 'build-essential' es un paquete muy útil para muchas compilaciones.
RUN apt-get update && apt-get install -y \
    python3-dev \
    build-essential \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# Establece las variables de entorno para una ejecución óptima en Docker
# No escribe archivos .pyc en el disco
ENV PYTHONDONTWRITEBYTECODE=1
# No almacena la salida en buffer
ENV PYTHONUNBUFFERED=1 

# Crea el directorio de la aplicación y lo establece como el directorio de trabajo
RUN mkdir /app
WORKDIR /app

# Copia solo el archivo de requerimientos para aprovechar el caching de Docker
COPY requirements.txt .

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de tu proyecto al contenedor
COPY . .

# Recopila los archivos estáticos para producción
RUN python manage.py collectstatic --noinput

# Expone el puerto por defecto de Render
EXPOSE 8080

# Comando para correr la aplicación en producción con Gunicorn
# Reemplaza 'project' por el nombre de tu proyecto Django
CMD ["gunicorn", "--bind", ":8080", "--workers", "2", "project.wsgi:application"]


