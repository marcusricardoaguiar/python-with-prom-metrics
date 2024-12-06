from flask import Blueprint, jsonify
from .main import REQUEST_COUNT,REQUEST_LATENCY

clients_bp = Blueprint('clients', __name__, url_prefix='/api')

# List all clients
@clients_bp.route('/clients')
def home():
    REQUEST_COUNT.labels(method='GET', endpoint='/clients').inc()  # Increment counter
    with REQUEST_LATENCY.labels(endpoint='/clients').time():  # Measure latency
        return jsonify({"clients": [{"name": "Joao"},{"name": "Jose"}]}), 200
