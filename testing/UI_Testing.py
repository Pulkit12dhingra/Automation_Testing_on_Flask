import unittest
from app import app
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Home', response.data)

    def test_about_page(self):
        response = self.app.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About', response.data)

    def test_contact_page(self):
        response = self.app.get('/contact')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Contact', response.data)

    def test_login_page(self):
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login', response.data)

    def test_register_page(self):
        response = self.app.get('/register')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Register', response.data)

if __name__ == '__main__':
    unittest.main()
    class TestUI(unittest.TestCase):

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

    if __name__ == '__main__':
        unittest.main()