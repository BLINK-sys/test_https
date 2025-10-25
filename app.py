# app.py
from flask import Flask, request, jsonify
import logging
import os

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/')
def health_check():
    """Проверка здоровья сервиса"""
    return jsonify({"status": "ok", "message": "HTTPS Test Server is running"}), 200

@app.route('/data', methods=['POST'])
def receive_data():
    """Эндпоинт для получения данных"""
    try:
        data = request.get_json(force=True)
    except Exception as e:
        app.logger.error("Invalid JSON: %s", e)
        return jsonify({"status":"error", "message":"invalid json"}), 400

    app.logger.info("Received data: %s", data)
    # тут можно сохранить в БД, в файл или обработать
    return jsonify({"status":"ok", "received": data}), 200

@app.route('/test', methods=['GET'])
def test_endpoint():
    """Тестовый эндпоинт"""
    return jsonify({
        "status": "ok", 
        "message": "Test endpoint working",
        "https_enabled": request.is_secure
    }), 200

if __name__ == "__main__":
    # Для разработки (HTTP). На проде — ставьте nginx / gunicorn, TLS и т.п.
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
