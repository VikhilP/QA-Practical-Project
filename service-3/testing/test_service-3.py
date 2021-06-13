from flask_testing import TestCase
from flask import url_for
from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_service3(self):
        response = self.client.get(url_for("pick"))

        self.assertIn(response.json, range(1,224))