import jwt
import datetime
import os
from dotenv import load_dotenv
from flask import jsonify
# Load the .env file
load_dotenv()

# Access the environment variables
SECRET_KEY = os.getenv('SECRET_KEY')



def jwt_encode(user_id, username):
    payload = {
        'user_id': user_id,
        'username': username,
        'exp': datetime.datetime.now() + datetime.timedelta(hours=24)
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

    return jsonify({"token":token})

def jwt_decode(token):
    SECRET_KEY = '123456789'
    try:
        decoded_payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return decoded_payload
    except jwt.ExpiredSignatureError:
        return "TOKEN_EXPIRED"
    except jwt.InvalidTokenError:
        return "INVALID_TOKEN"




