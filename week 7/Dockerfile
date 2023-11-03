# Usa una imagen base de Python
FROM python:3.9

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia solo el archivo practi3.py al contenedor
COPY practi4.py /app

# Instala las dependencias si tienes un archivo requirements.txt
COPY requirements.txt /app
RUN pip install -r requirements.txt

# Define el comando para ejecutar el script
CMD ["python", "practi4.py"]
