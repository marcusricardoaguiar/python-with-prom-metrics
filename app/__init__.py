from flask import Flask
# Register routes from routes.py
from .routes import main_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(main_bp)

    return app
