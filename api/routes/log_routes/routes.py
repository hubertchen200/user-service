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
        print(request.args)
        return get_logs(request.args.get('app_name'), request.args.get('log_type'), request.args.get('source'), request.args.get('date_from'), request.args.get('date_to'))


   