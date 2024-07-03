from api import create_app

app = create_app()


@app.route('/health')
def health():
    return "ok"

if __name__ == '__main__':
    app.run(debug=True, port=8081, host='0.0.0.0')