from . import user_bp
from flask import request, jsonify
from api.user import get_user, create_user, delete_user, sign_in
from hubertchen_package import my_jwt

@user_bp.route('/user', methods = [ 'GET', 'POST', 'DELETE'])
def my_user():
    if request.method == 'POST':
        user = request.get_json()
        result = create_user(user["email"], user["firstname"], user["lastname"], user["password"], user["username"])
        if 'error' in result.keys():
            return jsonify(result), 400
        return jsonify(result), 201
    data, code = my_jwt.check_token(request.headers)
    if code == 401:
        return jsonify(data), code
    if request.method == "GET":
        return get_user()
    elif request.method == 'DELETE':
        id = request.args.get("id", default=None, type=int)
        return delete_user(id)



@user_bp.route('/signin', methods = ['POST'])
def my_signin():

    if request.method == "POST":
        body = request.get_json()
        result = sign_in(body['email'], body['password'])
        if 'error' in result.keys():
            if 'password and/or email incorrect' == result['error']:
                return jsonify(result), 401
            return jsonify(result), 500
        return jsonify(result), 200
