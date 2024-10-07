from flask import Flask

print('api init')
from api.routes.user_routes import user_bp
from api.routes.jwt_routes import jwt_bp
from api.routes.log_routes import log_bp


def create_app():
    app = Flask(__name__)
    print('create app')
    app.register_blueprint(user_bp)
    app.register_blueprint(jwt_bp)
    app.register_blueprint(log_bp)
    return app
