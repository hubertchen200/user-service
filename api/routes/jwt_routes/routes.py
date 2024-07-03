from . import jwt_bp
from flask import request
from api.jwt_token.my_jwt import jwt_encode, jwt_decode
@jwt_bp.route('/token', methods = [ 'POST'])
def my_encode():
    payload = request.get_json()
    return jwt_encode(payload["user_id"], payload["username"])


