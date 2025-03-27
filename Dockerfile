FROM python:3.12-slim

# Установка cron и зависимостей
RUN apt-get update && apt-get install -y cron

# Копируем проект
WORKDIR /app
COPY . .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем крон-расписание
COPY crontab.txt /etc/cron.d/sync-cron

# Делаем файл исполняемым
RUN chmod 0644 /etc/cron.d/sync-cron

# Регистрируем cron-расписание
RUN crontab /etc/cron.d/sync-cron

# Создаём лог-файл
RUN touch /var/log/sync.log

# Команда запуска: cron + хвост логов
CMD ["sh", "-c", "cron && tail -f /var/log/sync.log"]