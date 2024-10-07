from api import create_app
from flask_cors import CORS
app = create_app()


CORS(app)

@app.route('/health')
def health():
    return "ok"

print(__name__)

if __name__ == '__main__':
    app.run(debug=True, port=8081, host='0.0.0.0')