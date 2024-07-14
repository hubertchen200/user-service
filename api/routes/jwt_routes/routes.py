from . import jwt_bp
from flask import request
from hubertchen_package import my_jwt
@jwt_bp.route('/token', methods = [ 'POST'])
def my_encode():
    payload = request.get_json()
    return my_jwt.jwt_encode(payload["user_id"], payload["username"])


