# Gunakan base image Python yang ringan
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Salin file requirements.txt dan instal dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Salin semua file aplikasi ke dalam container
COPY . /app/

# Expose port untuk aplikasi
EXPOSE 8080

# Perintah untuk menjalankan aplikasi menggunakan Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "run:app"]