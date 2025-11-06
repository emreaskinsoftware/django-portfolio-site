# Resmi Python imajını kullan
FROM python:3.11-slim

# Ortam değişkenleri
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Çalışma dizini oluştur
WORKDIR /app

# Gereksinimleri yükle
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Proje dosyalarını kopyala
COPY . /app/

# Django'nun default portu
EXPOSE 8000

# Uygulamayı çalıştır
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
