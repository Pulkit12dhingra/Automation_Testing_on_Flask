import unittest
import subprocess
import requests
import threading
from app import app
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from locust import HttpUser, TaskSet, task, between

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

class UITests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:5000")

    def test_home_page_title(self):
        self.assertIn("Home", self.driver.title)

    def test_about_page_navigation(self):
        self.driver.find_element(By.LINK_TEXT, "About").click()
        time.sleep(1)
        self.assertIn("About", self.driver.title)

    def test_contact_page_navigation(self):
        self.driver.find_element(By.LINK_TEXT, "Contact").click()
        time.sleep(1)
        self.assertIn("Contact", self.driver.title)

    def test_login_page_navigation(self):
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        time.sleep(1)
        self.assertIn("Login", self.driver.title)

    def test_register_page_navigation(self):
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        time.sleep(1)
        self.assertIn("Register", self.driver.title)

    def tearDown(self):
        self.driver.quit()

class UserBehavior(TaskSet):
    @task(1)
    def home(self):
        self.client.get("/")

    @task(2)
    def about(self):
        self.client.get("/about")

    @task(3)
    def contact(self):
        self.client.get("/contact")

    @task(4)
    def login(self):
        self.client.get("/login")

    @task(5)
    def register(self):
        self.client.get("/register")

class PerformanceTests(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)

class BrowserTests(unittest.TestCase):
    def test_on_grid(self, browser):
        if browser == 'chrome':
            options = webdriver.ChromeOptions()
        elif browser == 'firefox':
            options = webdriver.FirefoxOptions()
        else:
            raise ValueError(f"Unsupported browser: {browser}")

        driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            options=options
        )
        driver.get("http://localhost:5000")
        self.assertIn("Home", driver.title)
        driver.quit()

    def test_chrome(self):
        self.test_on_grid('chrome')

    def test_firefox(self):
        self.test_on_grid('firefox')

if __name__ == '__main__':
    try:
        # Run bandit for security testing
        print("Running Bandit for security testing...")
        subprocess.run(["bandit", "-r", "app.py"], check=True)

        # Run locust for performance testing
        print("Running Locust for performance testing...")
        locust_process = subprocess.Popen(["locust", "-f", "performance_testing.py"])

        # Load all test cases from the classes
        loader = unittest.TestLoader()
        suite = unittest.TestSuite()
        suite.addTests(loader.loadTestsFromTestCase(FlaskAppTests))
        suite.addTests(loader.loadTestsFromTestCase(RegressionTests))
        suite.addTests(loader.loadTestsFromTestCase(UITests))
        suite.addTests(loader.loadTestsFromTestCase(BrowserTests))

        # Run the test suite
        runner = unittest.TextTestRunner(verbosity=2)
        runner.run(suite)
    finally:
        # Ensure the Locust process is terminated
        locust_process.terminate()
        locust_process.wait()
        print("Locust process terminated.")