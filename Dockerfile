FROM python:3.12-slim

# Копирование проекта
WORKDIR /app
COPY . .

# Установка зависимотсей
RUN pip install --no-cache-dir -r requirements.txt

# Запуск сервера синхронизации
CMD ["python", "main.py"]