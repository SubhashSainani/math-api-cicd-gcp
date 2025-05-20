import unittest
from main import add_numbers, multiply_numbers, app

class TestMathFunctions(unittest.TestCase):
    def test_add_numbers_success(self):
        """Test that the add_numbers function works correctly."""
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)

    def test_add_numbers_failure(self):
        """This test is designed to fail."""
        self.assertEqual(add_numbers(2, 2), 5)  # Intentional failure

    def test_multiply_numbers_success(self):
        """Test that the multiply_numbers function works correctly."""
        self.assertEqual(multiply_numbers(2, 3), 6)
        self.assertEqual(multiply_numbers(-1, 1), -1)
        self.assertEqual(multiply_numbers(0, 5), 0)

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_route(self):
        """Test the home route returns the correct message."""
        response = self.app.get('/')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], "Hello, CI/CD on GCP!")

    def test_add_route(self):
        """Test the add route returns the correct result."""
        response = self.app.get('/add/2/3')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['result'], 5)

    def test_multiply_route(self):
        """Test the multiply route returns the correct result."""
        response = self.app.get('/multiply/2/3')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['result'], 6)

if __name__ == '__main__':
    unittest.main()