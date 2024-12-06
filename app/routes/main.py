from flask import Blueprint, render_template, jsonify
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

# Create Prometheus metrics
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP requests', ['method', 'endpoint'])
REQUEST_LATENCY = Histogram('http_request_duration_seconds', 'Latency of HTTP requests', ['endpoint'])

# Create a Blueprint
main_bp = Blueprint('main', __name__)

# Main route
@main_bp.route('/')
def home():
    REQUEST_COUNT.labels(method='GET', endpoint='/').inc()  # Increment counter
    with REQUEST_LATENCY.labels(endpoint='/').time():  # Measure latency
        return render_template('index.html')

# Hello sample route
@main_bp.route('/hello', methods=['GET'])
def hello():
    REQUEST_COUNT.labels(method='GET', endpoint='/hello').inc()  # Increment counter
    with REQUEST_LATENCY.labels(endpoint='/hello').time():  # Measure latency
        return jsonify({"message": "Hello from the API!"}), 200

# Data sample route
@main_bp.route('/api/data', methods=['GET'])
def get_data():
    REQUEST_COUNT.labels(method='GET', endpoint='/api/data').inc()  # Increment counter
    with REQUEST_LATENCY.labels(endpoint='/api/data').time():  # Measure latency
        return jsonify({"data": [1, 2, 3, 4]}), 200

# Path parameter route
@main_bp.route('/greet/<name>')
def greet(name):
    REQUEST_COUNT.labels(method='GET', endpoint='/greet/<name>').inc()  # Increment counter
    with REQUEST_LATENCY.labels(endpoint='/greet/<name>').time():  # Measure latency
        return jsonify({"message": f"Hello {name}!"}), 200

# Prometheus metrics route
@main_bp.route('/metrics')
def metrics():
    """Endpoint for Prometheus to scrape metrics"""
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}
