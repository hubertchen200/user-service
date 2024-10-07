from flask import request, jsonify
from api.logs import logs, get_logs
from . import log_bp
@log_bp.route('/log', methods = ['POST', 'GET'])
def log():
    if request.method == 'POST':
        data = request.get_json()
        result = logs(data)
        if 'error' in result.keys():
            return jsonify(result), 400
        return jsonify(result), 201
    if request.method == "GET":
        data = request.get_json()
        return get_logs(data["app_name"], data["log_type"], data["source"], data["date_from"], data["date_to"])


   