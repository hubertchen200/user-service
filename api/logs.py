from api.utils import get_connection
from flask import jsonify
def logs(log):
    try:
        set_default_values(log)
        conn = get_connection()
        cursor = conn.cursor()
        insert_query = "INSERT INTO logs (app_name,log_type, source, error, messages, status, data) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (log["app_name"], log["log_type"], log["source"], log["error"], log["messages"], log["status"], log["data"]))
        conn.commit()
        return {"status":"success"}
    except Exception as e:
        print(f"failed: {e}")
        return {"error": f"message: {e}"}

def get_logs(app_name, log_type, source, date_from, date_to):
    try:

        conn = get_connection()
        cursor = conn.cursor()
        select_query = "select * from logs where app_name = %s  and log_type = %s and source = %s and timestamp between %s and %s"
        select_data = (app_name, log_type, source, date_from, date_to)
        cursor.execute(select_query, select_data)
        rows = cursor.fetchall()
        logs = []
        for row in rows:
            log = {
                "app_name": row[0],
                "log_type": row[1],
                "source": row[2],
                "error": row[3],
                "messages": row[4],
                "status": row[5],
                "data": row[6],
                "timestamp": row[7]
            }
            logs.append(log)
        print(logs)
        return jsonify(logs)
    except Exception as e:
        print(f"failed: {e}")
        return {"error": f"message: {e}"}




def set_default_values(object):
    fields = ['app_name', 'log_type', 'source', 'error', 'messages', 'status', 'data']
    for field in fields:
        try:
            object[field]
        except:
            object[field] = 'null'

get_logs("app1", "temp", "alarm", "2024-10-06", "2024-10-9")




