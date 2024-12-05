import unittest
from app import create_app

class FlaskRoutesTestCase(unittest.TestCase):

    def setUp(self):
        """Set up test client before each test."""
        self.app = create_app()
        self.client = self.app.test_client()

    def tearDown(self):
        """Clean up after each test (if needed)."""

    def test_api_hello_route(self):
        """Test the API hello route."""
        response = self.client.get('/hello')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Hello from the API!", response.get_json()["message"])

    def test_api_data_route(self):
        """Test the API data route."""
        response = self.client.get('/api/data')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["data"], [1, 2, 3, 4])

    def test_api_greet_route(self):
        """Test the API greet route."""
        response = self.client.get('/greet/marcus')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Hello marcus!", response.get_json()["message"])

    def test_nonexistent_route(self):
        """Test a nonexistent route."""
        response = self.client.get('/nonexistent')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
