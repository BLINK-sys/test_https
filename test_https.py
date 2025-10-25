# app.py
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/data', methods=['POST'])
def receive_data():
    try:
        data = request.get_json(force=True)
    except Exception as e:
        app.logger.error("Invalid JSON: %s", e)
        return jsonify({"status":"error", "message":"invalid json"}), 400

    app.logger.info("Received data: %s", data)
    # С‚СѓС‚ РјРѕР¶РЅРѕ СЃРѕС…СЂР°РЅРёС‚СЊ РІ Р‘Р”, РІ С„Р°Р№Р» РёР»Рё РѕР±СЂР°Р±РѕС‚Р°С‚СЊ
    return jsonify({"status":"ok", "received": data}), 200

if __name__ == "__main__":
    # Р”Р»СЏ СЂР°Р·СЂР°Р±РѕС‚РєРё (HTTP). РќР° РїСЂРѕРґРµ вЂ” СЃС‚Р°РІСЊС‚Рµ nginx / gunicorn, TLS Рё С‚.Рї.
    app.run(host="0.0.0.0", port=5000, debug=True)
