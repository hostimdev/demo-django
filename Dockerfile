FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies for mysqlclient
RUN apk add --no-cache \
    mariadb-dev \
    gcc \
    musl-dev \
    pkgconf \
    jpeg-dev \
    zlib-dev \
    libjpeg


WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Create an entrypoint script to run migrations before starting the server
RUN echo '#!/bin/sh' > /entrypoint.sh && \
    echo 'python manage.py migrate --noinput' >> /entrypoint.sh && \
    echo 'python manage.py runserver 0.0.0.0:8000' >> /entrypoint.sh && \
    chmod +x /entrypoint.sh

CMD ["/entrypoint.sh"]
