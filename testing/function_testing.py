import unittest
import requests
from app import app
import threading

class FlaskAppTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Start the Flask app in a separate thread
        cls.server = threading.Thread(target=app.run, kwargs={'port': 5000})
        cls.server.start()

    @classmethod
    def tearDownClass(cls):
        # Shut down the Flask app and wait for the thread to finish
        requests.get('http://localhost:5000/shutdown')
        cls.server.join()

    def setUp(self):
        # Set up the test client for unit tests
        self.app = app.test_client()
        self.app.testing = True

    # Unit test for the home page
    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Home', response.data)

    # Unit test for the about page
    def test_about_page(self):
        response = self.app.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About', response.data)

    # Unit test for the contact page
    def test_contact_page(self):
        response = self.app.get('/contact')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Contact', response.data)

    # Unit test for the login page
    def test_login_page(self):
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login', response.data)

    # Unit test for the register page
    def test_register_page(self):
        response = self.app.get('/register')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Register', response.data)

    # Integration test for the home page
    def test_home_page_integration(self):
        response = requests.get('http://localhost:5000/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Home', response.text)

    # Integration test for the about page
    def test_about_page_integration(self):
        response = requests.get('http://localhost:5000/about')
        self.assertEqual(response.status_code, 200)
        self.assertIn('About', response.text)

    # Integration test for the contact page
    def test_contact_page_integration(self):
        response = requests.get('http://localhost:5000/contact')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Contact', response.text)

    # Integration test for the login page
    def test_login_page_integration(self):
        response = requests.get('http://localhost:5000/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Login', response.text)

    # Integration test for the register page
    def test_register_page_integration(self):
        response = requests.get('http://localhost:5000/register')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Register', response.text)

class RegressionTests(unittest.TestCase):

    def setUp(self):
        # Set up the test client for regression tests
        self.app = app.test_client()
        self.app.testing = True

    # Regression test for the home page
    def test_home_page_regression(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Home', response.data)

    # Regression test for the about page
    def test_about_page_regression(self):
        response = self.app.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About', response.data)

    # Regression test for the contact page
    def test_contact_page_regression(self):
        response = self.app.get('/contact')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Contact', response.data)

    # Regression test for the login page
    def test_login_page_regression(self):
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login', response.data)

    # Regression test for the register page
    def test_register_page_regression(self):
        response = self.app.get('/register')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Register', response.data)

if __name__ == '__main__':
    # Load all test cases from the classes
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(FlaskAppTests))
    suite.addTests(loader.loadTestsFromTestCase(RegressionTests))

    # Run the test suite
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)