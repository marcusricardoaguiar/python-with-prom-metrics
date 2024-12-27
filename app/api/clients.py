from .main import REQUEST_COUNT, REQUEST_LATENCY
from flask_restful import Resource
from ..models.clients import Client
from ..models.database import db

# List all clients
class ListClients(Resource):

    def get(self):
        REQUEST_COUNT.labels(method='GET', endpoint='/clients').inc()  # Increment counter
        with REQUEST_LATENCY.labels(method='GET', endpoint='/clients').time():  # Measure latency
            clients = Client.query.all()
            return [client.json() for client in clients], 200

class Clients(Resource):

    def get(self, name):
        REQUEST_COUNT.labels(method='GET', endpoint='/client/<string:name>').inc()  # Increment counter
        with REQUEST_LATENCY.labels(method='GET', endpoint='/client/<string:name>').time():  # Measure latency
            client = Client.query.filter_by(name=name).first()
            if client:
                return client.json()
            else:
                return {}, 404

    def post(self, name):
        REQUEST_COUNT.labels(method='POST', endpoint='/client').inc()  # Increment counter
        with REQUEST_LATENCY.labels(method='POST', endpoint='/client').time():  # Measure latency
            client = Client(name=name)
            db.session.add(client)
            db.session.commit()
            return client.json()

    def delete(self, name):
        REQUEST_COUNT.labels(method='DELETE', endpoint='/client').inc()  # Increment counter
        with REQUEST_LATENCY.labels(method='DELETE', endpoint='/client').time():  # Measure latency
            client = Client.query.filter_by(name=name).first()
            db.session.delete(client)
            db.session.commit()
            if client:
                return {'note': 'delete success'}
            else:
                return {'note': 'client does not exist'}
