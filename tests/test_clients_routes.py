import unittest

from flask_restful import Api

from app import app
from app.models.database import db

class FlaskRoutesTestCase(unittest.TestCase):

    def setUp(self):
        """Set up test client before each test."""
        self.app = app
        self.api = Api(self.app)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # In-memory database for testing
        self.app.config['TESTING'] = True
        self.client = app.test_client()
        self.client.testing = True
        # Create the database tables
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        """Clean up after each test (if needed)."""
        with self.app.app_context():
            # Drop all the tables after each test
            db.session.remove()
            db.drop_all()

    def test_api_list_clients_route(self):
        """Test the API list clients route."""
        response = self.client.get('/clients')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(0, len(response.get_json()))

    def test_api_add_client_route(self):
        """Test the API add client route."""
        response = self.client.post('/client', json={"name": "Marcus"})
        self.assertEqual(response.status_code, 200)

    def test_api_add_client_route_error(self):
        """Test the API add client route with wrong input data."""
        response = self.client.post('/client', json={})
        self.assertEqual(response.status_code, 400)

    def test_api_get_client_route(self):
        """Test the API get client route."""
        response = self.client.post('/client', json={"name": "Marcus"})
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/client/1')
        self.assertEqual(response.status_code, 200)

    def test_api_get_client_route_error(self):
        """Test the API get client route that does not exist in the database."""
        response = self.client.get('/client/1')
        self.assertEqual(response.status_code, 404)

    def test_api_delete_client_route(self):
        """Test the API delete client route."""
        response = self.client.post('/client', json={"name": "Marcus"})
        self.assertEqual(response.status_code, 200)
        response = self.client.delete('/client/1')
        self.assertEqual(response.status_code, 200)

    def test_api_delete_client_route_error(self):
        """Test the API delete client route that does not exist in the database."""
        response = self.client.delete('/client/1')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
