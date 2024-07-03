from flask import Flask

print('api init')
from api.routes.friend_routes import friend_bp
from api.routes.user_routes import user_bp
from api.routes.jwt_routes import jwt_bp
from api.routes.message_routes import message_bp

def create_app():
    app = Flask(__name__)
    print('create app')
    app.register_blueprint(friend_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(jwt_bp)
    app.register_blueprint(message_bp)
    return app
