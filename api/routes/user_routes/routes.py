from . import user_bp
from flask import request, jsonify
from api.user import get_user, create_user, delete_user, sign_in
from api.jwt_token.my_jwt import check_token

@user_bp.route('/user', methods = [ 'GET', 'POST', 'DELETE'])
def my_user():
    data, code = check_token(request.headers)
    if code == 401:
        return jsonify(data), code
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
    data, code = check_token(request.headers)
    if code == 401:
        return jsonify(data), code
    if request.method == "POST":
        body = request.get_json()
        return sign_in(body['email'], body['password'])
