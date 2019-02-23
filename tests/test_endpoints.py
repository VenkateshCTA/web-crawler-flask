from app import app
from flask import url_for
import unittest


class FlaskAppTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status_code(self):
        """Assert that user successfully lands on homepage"""
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_todo_creation(self):
        """Assert that user is redirected after creating todo item"""
        response = self.app.post('/results',
                                 data=dict(url="https://gale.agency/",
                                           depth=1)
                                 )
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
