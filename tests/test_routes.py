import unittest
from app import app
from app.models.database import db
from prometheus_client import CONTENT_TYPE_LATEST

class FlaskRoutesTestCase(unittest.TestCase):

    def setUp(self):
        """Set up test client before each test."""
        self.app = app
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # In-memory database for testing
        self.app.config['TESTING'] = True
        self.client = app.test_client()
        # Create the database tables
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        """Clean up after each test (if needed)."""
        with self.app.app_context():
            # Drop all the tables after each test
            db.session.remove()
            db.drop_all()

    def test_api_main_route(self):
        """Test the API main route."""
        response = self.client.get('/')
        print(response)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Hello World", response.get_json()["message"])

    def test_api_metrics_route(self):
        """Test the API metrics route."""
        response = self.client.get('/metrics')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, CONTENT_TYPE_LATEST)

    def test_nonexistent_route(self):
        """Test a nonexistent route."""
        response = self.client.get('/nonexistent')
        self.assertEqual(response.status_code, 404)

    def test_api_list_clients_route(self):
        """Test the API list clients route."""
        response = self.client.get('/clients')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(0, len(response.get_json()))

    def test_api_add_client_route(self):
        """Test the API add client route."""
        response = self.client.post('/client/marcus')
        self.assertEqual(response.status_code, 200)

    def test_api_get_client_route(self):
        """Test the API get client route."""
        response = self.client.post('/client/marcus')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/client/marcus')
        self.assertEqual(response.status_code, 200)

    def test_api_delete_client_route(self):
        """Test the API delete client route."""
        response = self.client.post('/client/marcus')
        self.assertEqual(response.status_code, 200)
        response = self.client.delete('/client/marcus')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
