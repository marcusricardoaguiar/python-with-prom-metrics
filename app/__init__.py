from flask import Flask

# Register routes from routes/main.py
from .routes.main import main_bp
# Register routes from routes/clients.py
from .routes.clients import clients_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(main_bp)
    app.register_blueprint(clients_bp)

    return app
