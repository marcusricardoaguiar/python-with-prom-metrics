from flask import make_response
from flask_restful import Resource
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST, Counter, Histogram

class Main(Resource):
    def get(self):
        REQUEST_COUNT.labels(method='GET', endpoint='/').inc()  # Increment counter
        with REQUEST_LATENCY.labels(method='GET', endpoint='/').time():  # Measure latency
            return {"message": "Hello World"}, 200

########################
### PROMETHEUS SETUP ###
########################
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP requests', ['method', 'endpoint'])
REQUEST_LATENCY = Histogram('http_request_duration_seconds', 'Latency of HTTP requests', ['method', 'endpoint'])

# Prometheus metrics route
class Metrics(Resource):
    """Endpoint for Prometheus to scrape metrics"""

    def get(self):
        # Create a response with plain text and set the Content-Type
        response = make_response(generate_latest(), 200)
        response.headers['Content-Type'] = CONTENT_TYPE_LATEST
        return response
