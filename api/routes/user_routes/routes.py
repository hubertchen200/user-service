from . import user_bp
from flask import request, jsonify
from api.user import get_user, create_user, delete_user, sign_in
from api.jwt_token.my_jwt import jwt_decode

@user_bp.route('/user', methods = [ 'GET', 'POST', 'DELETE'])
def my_user():
    token = request.headers.get('Authorization')
    token = token.replace("Bearer ", "")
    payload = jwt_decode(token)
    if payload == "TOKEN_EXPIRED":
        return jsonify({'error':"TOKEN_EXPIRED"})
    if payload == "INVALID_TOKEN":
        return jsonify({'error':'INVALID_TOKEN'})
    if request.method == "GET":
        return get_user()
    elif request.method == 'POST':
        user = request.get_json()
        return create_user(user["email"], user["firstname"], user["lastname"], user["password"], user["username"])
    elif request.method == 'DELETE':
        id = request.args.get("id", default=None, type=int)
        return delete_user(id)



@user_bp.route('/signin', methods = ['POST'])
def my_signin():
    token = request.headers.get('Authorization')
    token = token.replace("Bearer ", "")
    payload = jwt_decode(token)
    if payload == "TOKEN_EXPIRED":
        return jsonify({'error': "TOKEN_EXPIRED"})
    if payload == "INVALID_TOKEN":
        return jsonify({'error': 'INVALID_TOKEN'})
    if request.method == "POST":
        body = request.get_json()
        return sign_in(body['email'], body['password'])
