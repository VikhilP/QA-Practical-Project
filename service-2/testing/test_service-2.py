from flask_testing import TestCase
from flask import url_for
# from service-2.app import app, pos
from app import app, pos

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_service_2(self):
        
        response = self.client.get(url_for("pos"))

        positions = ["SS","1B","2B","3B","LF","RF","CF","DH","C"]
        self.assertIn(response.data.decode(), positions)