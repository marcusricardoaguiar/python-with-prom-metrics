from .clients import Clients, ListClients
from .main import Metrics, Main

def initialize_routes(api):
    # Add resources to the API and map them to the corresponding URLs
    api.add_resource(Main, '/')
    api.add_resource(Metrics, '/metrics')
    api.add_resource(ListClients, '/clients')
    api.add_resource(Clients, '/client/<string:name>')
