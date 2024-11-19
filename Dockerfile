# Usa una imagen base ligera
FROM python:3.10-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia las dependencias y las instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todos los archivos del proyecto
COPY . .

# Expone el puerto 8000 para la aplicación
EXPOSE 8000

# Comando predeterminado para ejecutar el servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
