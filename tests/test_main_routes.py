import unittest

from flask_restful import Api
from prometheus_client import CONTENT_TYPE_LATEST

from app import app

class FlaskRoutesTestCase(unittest.TestCase):

    def setUp(self):
        """Set up test client before each test."""
        self.app = app
        self.api = Api(self.app)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # In-memory database for testing
        self.app.config['TESTING'] = True
        self.client = app.test_client()
        self.client.testing = True

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

if __name__ == '__main__':
    unittest.main()
