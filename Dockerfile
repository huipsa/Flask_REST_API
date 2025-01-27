FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Применяем миграции перед запуском
CMD flask db upgrade && flask run --host=0.0.0.0
