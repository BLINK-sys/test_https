# HTTPS Test Server

Простой Flask сервер для тестирования HTTPS соединений.

## Эндпоинты

- `GET /` - Проверка здоровья сервиса
- `POST /data` - Прием данных (JSON)
- `GET /test` - Тестовый эндпоинт с проверкой HTTPS

## Локальный запуск

```bash
pip install -r requirements.txt
python test_https.py
```

## Развертывание на Render

1. Подключите репозиторий к Render
2. Выберите тип сервиса "Web Service"
3. Укажите:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn test_https:app`
4. Render автоматически обеспечит HTTPS

## Тестирование

```bash
# Проверка здоровья
curl https://your-app.onrender.com/

# Тест эндпоинт
curl https://your-app.onrender.com/test

# Отправка данных
curl -X POST https://your-app.onrender.com/data \
  -H "Content-Type: application/json" \
  -d '{"test": "data"}'
```
