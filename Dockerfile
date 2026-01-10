# Usamos una imagen ligera de Python
FROM python:3.9-slim

# Creamos una carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copiamos nuestro script al contenedor
COPY app.py .

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
