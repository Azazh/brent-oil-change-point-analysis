import unittest
from src.app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_prices_endpoint(self):
        response = self.app.get('/api/prices')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()