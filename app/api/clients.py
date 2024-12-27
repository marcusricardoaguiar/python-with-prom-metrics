import time

from flask import request
from flask_restful import Resource

from .main import REQUEST_COUNT, REQUEST_LATENCY
from ..models.clients import Client
from ..models.database import db

# List all clients
class ListClients(Resource):

    def get(self):
        REQUEST_COUNT.labels(method='GET', endpoint='/clients', status_code=200).inc()  # Increment counter
        with REQUEST_LATENCY.labels(method='GET', endpoint='/clients', status_code=200).time():  # Measure latency
            clients = Client.query.all()
            return [client.json() for client in clients], 200

class Clients(Resource):
    def get(self, id):
        # Start measuring the request duration
        start_time = time.time()
        client = Client.query.filter_by(id=id).first()
        if client:
            REQUEST_COUNT.labels(method='GET', endpoint='/client', status_code=200).inc()  # Increment counter
            # Calculate the request duration
            duration = time.time() - start_time
            REQUEST_LATENCY.labels(method='GET', endpoint='/client', status_code=200).observe(duration)  # Measure latency
            return client.json()
        else:
            REQUEST_COUNT.labels(method='GET', endpoint='/client', status_code=404).inc()  # Increment counter
            # Calculate the request duration
            duration = time.time() - start_time
            REQUEST_LATENCY.labels(method='GET', endpoint='/client', status_code=404).observe(duration)  # Measure latency
            return {}, 404

    def delete(self, id):
        # Start measuring the request duration
        start_time = time.time()
        client = Client.query.filter_by(id=id).first()
        db.session.delete(client)
        db.session.commit()
        if client:
            REQUEST_COUNT.labels(method='DELETE', endpoint='/client', status_code=200).inc()  # Increment counter
            # Calculate the request duration
            duration = time.time() - start_time
            REQUEST_LATENCY.labels(method='DELETE', endpoint='/client', status_code=200).observe(duration)  # Measure latency
            return {'note': 'delete success'}
        else:
            REQUEST_COUNT.labels(method='DELETE', endpoint='/client', status_code=404).inc()  # Increment counter
            # Calculate the request duration
            duration = time.time() - start_time
            REQUEST_LATENCY.labels(method='DELETE', endpoint='/client', status_code=404).observe(duration)  # Measure latency
            return {'note': 'client does not exist'}

class NewClient(Resource):

    def post(self):
        # Start measuring the request duration
        start_time = time.time()
        # Retrieve JSON data from the body of the request
        data = request.get_json()
        # Check if data is provided
        if not data:
            REQUEST_COUNT.labels(method='POST', endpoint='/client', status_code=400).inc()  # Increment counter
            # Calculate the request duration
            duration = time.time() - start_time
            REQUEST_LATENCY.labels(method='POST', endpoint='/client', status_code=400).observe(duration)  # Measure latency
            return {'message': 'No data provided'}, 400

        # Extract data
        name = data.get('name', None)

        client = Client(name)
        db.session.add(client)
        db.session.commit()
        REQUEST_COUNT.labels(method='POST', endpoint='/client', status_code=200).inc()  # Increment counter
        # Calculate the request duration
        duration = time.time() - start_time
        REQUEST_LATENCY.labels(method='POST', endpoint='/client', status_code=200).observe(duration)  # Measure latency
        return client.json()
