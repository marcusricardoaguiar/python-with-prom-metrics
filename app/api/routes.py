from .clients import Clients, NewClient, ListClients
from .main import Metrics, Main

def initialize_routes(api):
    # Add resources to the API and map them to the corresponding URLs
    api.add_resource(Main, '/')
    api.add_resource(Metrics, '/metrics')
    api.add_resource(ListClients, '/clients')
    api.add_resource(Clients, '/client/<int:id>')
    api.add_resource(NewClient, '/client')
