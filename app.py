from flask import Flask, request, jsonify
import psutil

app = Flask(__name__)

from config import app_config

SECRET_TOKEN = app_config.API_TOKEN

@app.route('/disk_space', methods=['GET'])
def get_disk_space():
    provided_token = request.headers.get('Authorization')
    if provided_token != f"Bearer {SECRET_TOKEN}":
        return jsonify({"error": "Token inválido"}), 401

    server_name = request.args.get('server_name')
    server_path = request.args.get('server_path')

    try:
        disk_usage = psutil.disk_usage('../')
        response = {
            "server": server_name,
            "path": server_path,
            "usage_percent": disk_usage.percent
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
