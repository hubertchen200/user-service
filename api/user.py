from api.utils import get_connection
from flask import jsonify
import bcrypt
import json



def get_user():
    conn = get_connection()

    cursor = conn.cursor()
    # Example query
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    users = []
    for row in rows:
        user = {
            "id": row[0],
            "email": row[1],
            "first_name": row[2],
            "last_name": row[3]
        }
        users.append(user)
    print(json.dumps(users, indent=4))
    return json.dumps(users)


# get_user()

def create_user(email, firstname, lastname, password, username):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        hashed_bytes = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        hashed = hashed_bytes.decode('utf-8')
        insert_query = "INSERT INTO users (email, first_name, last_name, password_hash, username) VALUES (%s, %s, %s, %s, %s)"
        user_data = (email, firstname, lastname, hashed, username)
        cursor.execute(insert_query, user_data)
        conn.commit()
        return {"status":"success"}
    except Exception as e:
        print(f"failed: {e}")
        data = {"error": f"message: {e}"}
        return data


# create_user("abc", "abc", "abc", "abc")
def delete_user(id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM users WHERE id = %s', (id,))
        conn.commit()
        print('success')
        data = {"status": "Success"}
        return jsonify(data)
    except Exception as e:
        data = {"error": f"message: {e}"}
        return jsonify(data)
# delete_user(5)


def sign_in(email, password):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT password_hash, first_name, last_name, email, username FROM users where (email = %s or username = %s)', (email, email))
        users = cursor.fetchall()
        if len(users) == 1:
            hashed_password = users[0][0].encode('utf-8')
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                return jsonify({'status':'success', "data":{
                    "firstname": users[0][1],
                    "lastname": users[0][2],
                    "email": users[0][3],
                    "username": users[0][4]
                }
                })
        return jsonify({'error':'password and email incorrect'})
    except Exception as e:
        data = {"error": f"message: {e}"}
        return jsonify(data)

# print(sign_in('abc@gmail.com', '1234'))

