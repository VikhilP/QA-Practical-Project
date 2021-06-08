from flask_testing import TestCase
from flask import url_for
import requests
from requests_mock import mock
from application import app, db
from application.models import GenerateDraft

class TestBase(TestCase):
    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
        app.config['SECRET_KEY'] = "dfs"
        app.config['WTF_CSRF_ENABLED'] = False
        db.drop_all()
        db.create_all()
        return app

class TestResponse(TestBase):
    def test_index(self):
        with mock() as m:
            form = GenerateDraft
            m.get('http://service_2:5001/getpositions', text='QB')
            m.get('http://service_3:5002/getpickorder', json=35)
            m.post('http://service_4:5003/round', json={'position': 'QB','draft_number': 35, 'draft_round': 2, 'round_pick': 3})

            response = self.client.post(url_for("home"))

            
            

        self.assert200(response)
        self.assertIn("QB", response.data.decode())

